function previewVideo(event) {
  const video = document.getElementById('videoPreview');
  const file = event.target.files[0];

  if (file) {
    const reader = new FileReader();
    reader.onload = function(event) {
      video.src = event.target.result;
      video.style.display = 'block';
    };
    reader.readAsDataURL(file);
  }
}
