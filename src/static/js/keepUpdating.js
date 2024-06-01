const list = document.getElementById("fancylist");
const ws = new WebSocket("ws://" + window.location.host + "/ws");
ws.onmessage = function(event) {
    let items = JSON.parse(event.data);
    while (list.firstChild) {
        list.removeChild(list.lastChild);
    }

    //
    for (const key in items) {
        let li = document.createElement("li");
        let tag = document.createElement("b")
        tag.appendChild(document.createTextNode(key + ": "))
        li.appendChild(tag)

        li.appendChild(document.createTextNode(items[key]));
        list.appendChild(li);
    }
}
