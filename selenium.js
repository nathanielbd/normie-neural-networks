var webdriver = require('selenium-webdriver')
var browser = new webdriver.Builder()
    .usingServer().withCapabilities({'browserName': 'chrome'})
    .build()

browser.get('http://dulm.blue/normie')
var values = []
for (var i = 1; i < 36; i++) {
    browser.findElements(webdriver.By.css(`.question > input[name='q${i}']`).then(
        inputs => {
            var to_select = inputs[Math.floor(Math.random()*inputs.length)];
            to_select.click();
            values.push(to_select.value)
        }
    ))
}
for (var j = 36; j < 42; j++) {
    $(`#q${j}`).selectedIndex = Math.floor(Math.random()*document.querySelectorAll(`#q${j} > option`).length)
    var to_select = document.querySelectorAll(`#q${j} > option`)[$(`#q${j}`).selectedIndex]
    values.push(to_select.value)
}
// we're not answering honestly
$('#honest').selectedIndex = 1
// fill out Robot test first
console.log(values.toString())
