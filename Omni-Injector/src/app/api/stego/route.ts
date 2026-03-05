import { NextResponse } from 'next/server';
import { embedDataIntoImage } from '@/lib/stego';

export async function POST(request: Request) {
    try {
        const formData = await request.formData();
        const imageFile = formData.get('image') as File | null;
        const payload = formData.get('payload') as string | null;

        if (!imageFile || !payload) {
            return NextResponse.json({ error: 'Missing image or payload' }, { status: 400 });
        }

        const imageBuffer = Buffer.from(await imageFile.arrayBuffer());

        // Embed the payload using LSB (Least Significant Bit) logic
        const stegoBuffer = await embedDataIntoImage(imageBuffer, payload);

        return new NextResponse(new Uint8Array(stegoBuffer), {
            status: 200,
            headers: {
                'Content-Type': 'image/png',
                'Content-Disposition': 'attachment; filename="payload_injected.png"',
            },
        });

    } catch (err: unknown) {
        if (err instanceof Error) {
            return NextResponse.json({ error: err.message }, { status: 500 });
        }
        return NextResponse.json({ error: 'Unknown server error' }, { status: 500 });
    }
}
