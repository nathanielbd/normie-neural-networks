var values = []
for (var i = 1; i < 36; i++) {
    var to_select = document.querySelectorAll(`.question > input[name='q${i}']`)[Math.floor(Math.random()*document.querySelectorAll(`.question > input[name='q${i}']`).length)]
    to_select.click()
    values.push(to_select.value)
}
// document.querySelector('.question > input[value="male"]').click()
// for (var j = 36; j < 42; j++) {
//     $(`#q${j}`).selectedIndex = 0
// }
for (var j = 36; j < 42; j++) {
    var to_select = document.querySelectorAll(`#q${j} > option`)[Math.floor(Math.random()*document.querySelectorAll(`#q${j} > option`).length)]
    to_select.click()
    values.push(to_select.value)
}
// we're not answering honestly
$('#honest').selectedIndex = 1
// fill out Robot test first
// $('[type="submit"]').click()
// console.log(values.slice(0,-6).toString())
console.log(values.toString())