const flashed = document.querySelectorAll(".flashed");
flashed.forEach((element) => {
  element.addEventListener("click", () => {
    element.style.display = "none";
  });
});

function toggle(className) {
  const all_tabs = document.querySelectorAll(className);
  all_tabs.forEach((element) => {
    if (element.lastElementChild.classList[1] == "open") {
      element.lastElementChild.classList.remove("open");
      element.firstElementChild.classList.remove("open_");
    } else {
      element.lastElementChild.classList.add("open");
      element.firstElementChild.classList.add("open_");
    }
  });
}

function open(className) {
  const all_tabs = document.querySelectorAll(className);
  all_tabs.forEach((element) => {
    if (!element.lastElementChild.classList[1]) {
      element.lastElementChild.classList.add("open");
      element.firstElementChild.classList.add("open_");
    }
  });
}

function close(className) {
  const all_tabs = document.querySelectorAll(className);
  all_tabs.forEach((element) => {
    if (element.lastElementChild.classList[1]) {
      element.lastElementChild.classList.remove("open");
      element.firstElementChild.classList.remove("open_");
    }
  });
}
