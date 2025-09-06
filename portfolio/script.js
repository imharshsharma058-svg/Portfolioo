const roles = ["Web Developer", "Student", "Tech Enthusiast"];
let i = 0;
let j = 0;
let currentRole = "";
let isDeleting = false;
const speed = 100;
const target = document.getElementById("typewriter");

function type() {
  if (i < roles.length) {
    if (!isDeleting && j <= roles[i].length) {
      currentRole = roles[i].substring(0, j++);
      target.innerHTML = "> " + currentRole;
    }

    if (isDeleting && j >= 0) {
      currentRole = roles[i].substring(0, j--);
      target.innerHTML = "> " + currentRole;
    }

    if (j === roles[i].length) {
      isDeleting = true;
      setTimeout(type, 1000);
      return;
    }

    if (isDeleting && j === 0) {
      isDeleting = false;
      i = (i + 1) % roles.length;
    }

    setTimeout(type, speed);
  }
}

type();
