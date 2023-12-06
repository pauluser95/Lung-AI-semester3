function test(){
  const form = document.querySelector('form');
  form.addEventListener('submit', (e) => {
      
      e.preventDefault();
      // Prevents HTML handling submission
      const name = document.getElementById("name");
      const files = document.getElementById("files");
      const formData = new FormData();
      // Creates empty formData object
      // formData.append("name", name.value);
      // Appends value of text input
      document.getElementById("predict").innerText='testing';
      formData.append("files", files.files[0]);
      // Appends value(s) of file input
      // Post data to Node and Express server:
      console.log(...formData);
      console.log(files.files[0]['name']);
      predictor(files.files[0]['name']);
      fetch('http://127.0.0.1:5000/api', {
          method: 'POST',
          body: formData, // Payload is formData object
      })
      .then(res => res.json())
      .then(data => console.log(data));
  })

}

async function predictor(filename){
  var text;
  console.log(filename)
  fetch('http://127.0.0.1:5000/predict', {
    method: 'POST',
    headers:{
      'Content-Type':'application/json'
    },
    body:JSON.stringify({a:filename}),
}).then(res=>res.json()).then(data=>{text=data['message'];}).then(()=>document.getElementById("predict").innerHTML=text);
// fetch('http://127.0.0.1:5000/predict', {
//   method: 'GET',
// }).then(res=>res.sed()).then(data=>{text=data;}).then(()=>document.getElementById("predict").innerText=text);
}

function init(){
  document.getElementById('form').onsubmit = test();
}
window.onload = init;





