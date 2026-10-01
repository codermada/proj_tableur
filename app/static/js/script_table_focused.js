const hide_result = document.getElementById("hide_result");
hide_result.addEventListener("click", () => {
  const hide_result = document.getElementById("hide_result");
  const rows = document.querySelectorAll(".tr");
  rows.forEach((element) => {
    let lastColumn = element.lastElementChild;
    let firstColumn = element.firstElementChild;
    if (lastColumn.style.display != "block") {
      lastColumn.style.display = "block";
      firstColumn.style.display = "block";
      hide_result.innerText = "hide results";
    } else {
      lastColumn.style.display = "none";
      firstColumn.style.display = "none";
      hide_result.innerText = "show results";
    }
  });
});
