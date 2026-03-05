/**
 * P4RS3LT0NGV3 Obfuscation Engine Adapter
 * Applies advanced unicode manipulations like Zalgo text.
 */

export function toZalgo(text: string): string {
    const zalgoUp = ['\u030d', '\u030e', '\u0304', '\u0305'];
    const zalgoDown = ['\u0316', '\u0317', '\u0318', '\u0319'];
    const zalgoMid = ['\u0315', '\u031b', '\u0340', '\u0341'];

    return text.split('').map(char => {
        if (char === ' ' || char === '\n') return char;
        let result = char;
        // Add random diacritics
        const rand = () => Math.floor(Math.random() * 4);
        result += zalgoUp[rand()];
        result += zalgoMid[rand()];
        result += zalgoDown[rand()];
        return result;
    }).join('');
}

export function toInvisible(text: string): string {
    // Uses Unicode Tags block to create completely invisible text strings
    // Base char is U+E0000 (Language Tag), offsets map ASCII to E0020-E007E
    let invisible = '';
    for (let i = 0; i < text.length; i++) {
        const code = text.charCodeAt(i);
        if (code >= 32 && code <= 126) {
            invisible += String.fromCodePoint(0xE0000 + code);
        } else {
            invisible += text[i];
        }
    }
    return invisible;
}
