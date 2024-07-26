document.getElementById("id_photo").addEventListener('change', (event) => {
  if (event.target.files && event.target.files[0]) {
      let reader = new FileReader();

      reader.onload = function(e) {
          document.getElementById('photoPreview').src = e.target.result;
      };

      reader.readAsDataURL(event.target.files[0]);
  }
});