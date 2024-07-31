const toast = window.document.getElementById("toastBar");
toast.classList.add("show")

setTimeout(() => {
  toast.className = toast.className.replace("show", "");
}, 3000);
