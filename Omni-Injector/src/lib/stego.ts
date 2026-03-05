import { PNG } from 'pngjs';

/**
 * Embeds a string payload into the Least Significant Bits (LSB) of a PNG image.
 * This effectively hides text within the color data of an image, similar to STEGOSAURUS-WRECKS.
 */
export async function embedDataIntoImage(imageBuffer: Buffer, payload: string): Promise<Buffer> {
    return new Promise((resolve, reject) => {
        new PNG().parse(imageBuffer, function (error, data) {
            if (error) {
                return reject(error);
            }

            const binaryPayload = stringToBinary(payload + '\0');
            let bitIndex = 0;

            // pngjs gives us a 1D array of RGBA values [r,g,b,a, r,g,b,a...]
            for (let idx = 0; idx < data.data.length; idx += 4) {
                for (let colorOffset = 0; colorOffset < 3; colorOffset++) { // only RGB, skip Alpha (+3)
                    if (bitIndex < binaryPayload.length) {
                        let channelValue = data.data[idx + colorOffset];
                        const targetBit = binaryPayload[bitIndex] === '1' ? 1 : 0;

                        // Force the least significant bit to match our target bit
                        channelValue = targetBit === 1 ? (channelValue | 1) : (channelValue & ~1);

                        data.data[idx + colorOffset] = channelValue;
                        bitIndex++;
                    }
                }
            }

            if (bitIndex < binaryPayload.length) {
                return reject(new Error(`Payload is too large for this image. Needed ${binaryPayload.length} bits, only had room for ${bitIndex}. Use a larger image or smaller payload.`));
            }

            // Pack the modified PNG back into a buffer
            const chunks: Buffer[] = [];
            data.pack()
                .on('data', (chunk) => chunks.push(chunk))
                .on('end', () => resolve(Buffer.concat(chunks)))
                .on('error', (err) => reject(err));
        });
    });
}

function stringToBinary(text: string): string {
    let output = '';
    for (let i = 0; i < text.length; i++) {
        const bin = text.charCodeAt(i).toString(2);
        output += bin.padStart(8, '0');
    }
    return output;
}
