/**
 * index.html dan A4 PDF yasaydi.
 *   node generate_pdf.js
 * Avval: python3 build.py
 */
const { execSync } = require('child_process');
const path = require('path');
const fs = require('fs');

const inputHtml = path.resolve(__dirname, 'index.html');
const outputPdf = path.resolve(__dirname, 'Kartochkalar_shabloni.pdf');

if (!fs.existsSync(inputHtml)) {
  console.error('index.html topilmadi. Avval: python3 build.py');
  process.exit(1);
}

const chrome = ['google-chrome', 'google-chrome-stable', 'chromium', 'chromium-browser']
  .find((bin) => {
    try { execSync(`command -v ${bin}`, { stdio: 'ignore' }); return true; }
    catch (e) { return false; }
  });

if (!chrome) { console.error('Chrome/Chromium topilmadi.'); process.exit(1); }

const cmd = [
  `${chrome} --headless --disable-gpu --no-sandbox`,
  '--no-pdf-header-footer --run-all-compositor-stages-before-draw',
  '--virtual-time-budget=20000',
  `--print-to-pdf="${outputPdf}"`,
  `"file://${inputHtml}"`,
].join(' ');

try {
  execSync(cmd, { stdio: ['ignore', 'ignore', 'pipe'] });
  const kb = (fs.statSync(outputPdf).size / 1024).toFixed(0);
  console.log(`Tayyor: ${path.basename(outputPdf)} (${kb} KB)`);
} catch (err) {
  console.error('PDF yig‘ishda xato:', err.message);
  process.exit(1);
}
