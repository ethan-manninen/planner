const hour = new Date().getHours();
const x = 13;
let greeting;
    if (0 < hour && hour < 12) {
        greeting = "Good Morning";
    } else if (12 <= hour && hour <= 17) {
        greeting = "Good Afternooon!";
    } else {
        greeting = "Good Evening!";
    }
    document.getElementById("greeting").innerHTML = greeting;
/*
    const alert_div = document.createElement("div");
    alert_div.setAttribute("class", "alert");

    const alert_container = document.getElementById("alerts");
    alert_container.appendChild(alert_div);
*/
async function getData() {
    const url = "http://localhost:1337/data.json";
    try {
      const response = await fetch(url);
      if (!response.ok) {
        throw new Error(`Response status: ${response.status}`);
      }
  
      const json = await response.json();
      console.log(json);
    } catch (error) {
      console.error(error.message);
    }
  }
/*
async function getXArtical(x) {
  const url = "http://localhost:1337/data.json";
    try {
      const response = await fetch(url);
      if (!response.ok) {
        throw new Error(`Response status: ${response.status}`);
      }
  
      const json = await response.json();
      const parsed = JSON.parse(json)
      return parsed[x];
    } catch (error) {
      console.error(error.message);
    }
}
*/

document.getElementById("alert_description").innerHTML = "THE AWESOME DESCRIPTIVE TEXT THAT NEEDS TO BE LONG ENOUGH TO WRAP AND IS ALSO UPDATED FROM JS";