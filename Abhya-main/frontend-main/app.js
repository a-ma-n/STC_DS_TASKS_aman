const list =document.querySelector('model');

db.collection('model').doc('fight').get().then((doc)=>
{
  console.log(doc.data())
var x=doc.data().fight
if (x==true){
  window.alert("Alert");
  window.open('cam1.html')
}

})
