// Script to download all inputs for the puzzles
//
// Instruction
// 1. Open https://adventofcode.com/ and login
// 2. Open developer tool window (in the browser)
// 3. Copy & Paste the code below into the console
// 4. Download and extract the zip
import('https://cdnjs.cloudflare.com/ajax/libs/jszip/3.10.1/jszip.min.js').then(async (zip) => {
  const headers = new Headers({ "User-Agent": "github.com/" });
  var zip = new JSZip();
  let year = 2015;
  let run = true;
  while (run) {
    var folder = zip.folder(`${year}`).folder('input');
    for (let day = 1 ; day <= 25 ; day++) {
      const url = `https://adventofcode.com/${year}/day/${day}/input`;
      const response = await fetch(url, { headers: headers });
      if (!response.ok) {
        run = false;
        break;      
      }
      else {
        let dayNo = String(day).padStart(2, '0');
        console.log(`Fetched ${year} day ${dayNo}`);
        folder.file(`${dayNo}.txt`, await response.text());
      }
    }
    year += 1;
  }
  zip.generateAsync({type:"blob"})
  .then(function(content) {
    const fileURL = URL.createObjectURL(content);
    const downloadLink = document.createElement('a');
    downloadLink.href = fileURL;
    downloadLink.download = 'input.zip';
    document.body.appendChild(downloadLink);
    downloadLink.click();
  });
});