const { readFileSync, writeFileSync } = require("fs");

const filepath = "./build/index.html";
const data = readFileSync(filepath, "utf-8")
    .replace(
        RegExp('="/static(/.*?)"', 'g'),
        `="{% static '$1' %}"`
    );
writeFileSync(filepath, "{% load static %}" + data)
console.log("\n\n The file has been statico-djanged !!\n\n");