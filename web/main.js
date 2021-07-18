window.onresize = function () {
  window.resizeTo(700, 700);
};

eel.expose(consoleArea);
function consoleArea(text) {
  area = document.getElementById("console");
  area.value += text + " \n";
}

let btn = document.querySelector("#btn");
btn.addEventListener("click", parser);

async function parser() {
  let url = document.querySelector("#url").value;
  let chapterNumbers = document.querySelector("#chapterNumbers").value;
  let outputFolder = document.querySelector("#outputFolder").value;
  let outputName = document.querySelector("#outputName").value;
  let firstChapter = document.querySelector("#firstChapter").value;
  let volumeNumber = document.querySelector("#volumeNumber").value;
  let area = document.querySelector("#console");
  area.value = "";
  await eel.start(
    url,
    chapterNumbers,
    outputFolder,
    outputName,
    firstChapter,
    volumeNumber
  );
}
