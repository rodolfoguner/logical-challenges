const input = require("fs").readFileSync("./stdin", "utf8");
const lines = input.split("\n");

function validInput(pagesReadPerDay, daysAdvantage, actualPagesRead) {
  return !(
    pagesReadPerDay < 0 ||
    pagesReadPerDay > 20 ||
    daysAdvantage < 0 ||
    daysAdvantage > 20 ||
    actualPagesRead < 0 ||
    actualPagesRead > 20
  );
}

for (const line of lines) {
  if (line === "0") {
    break;
  }

  const [pagesReadPerDay, daysAdvantage, actualPagesRead] = line
    .split(" ")
    .map((item) => parseInt(item));

  if (!validInput(pagesReadPerDay, daysAdvantage, actualPagesRead)) {
    break;
  }

  pages = Math.floor(
    (pagesReadPerDay * daysAdvantage * actualPagesRead) /
      (actualPagesRead - pagesReadPerDay)
  );

  if (pages <= 1) {
    console.log(`${pages} pagina`);
  } else {
    console.log(`${pages} paginas`);
  }
}
