const hide_result = document.getElementById("hide_result");
const rows = document.querySelectorAll(".tr");
rows.forEach((element) => {
  element.lastElementChild.style.display = "block";
  element.lastElementChild.style.border = "0px";
  element.lastElementChild.style.marginLeft = "5px";
});
hide_result.addEventListener("click", () => {
  const hide_result = document.getElementById("hide_result");
  const rows = document.querySelectorAll(".tr");
  rows.forEach((element) => {
    let lastColumn = element.lastElementChild;
    if (lastColumn.style.display != "block") {
      element.lastElementChild.style.display = "block";
      hide_result.innerText = "hide results";
    } else {
      element.lastElementChild.style.display = "none";
      hide_result.innerText = "show results";
    }
  });
});
