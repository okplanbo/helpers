$(function () {
    // Duplicate line exterminator
    $("#remove-duplicates").click(function () {
        var strings = $("#strings")
            .val()
            .split(/[\r\n]+/);
        var unique = [];
        top: for (var i in strings) {
            for (var j in unique) {
                if (strings[i] == unique[j]) {
                    continue top;
                }
            }
            unique.push(strings[i]);
        }
        $("#strings").val(unique.join("\r\n"));
    });
    // Censor
    $("#remove-words").click(function () {
        var strings = $("#from-what-to-cut")
            .val()
            .split(/[\r\n]+/);
        var del = $("#what-to-cut")
            .val()
            .split(/[\r\n]+/);
        var unique = [];
        top: for (var i in strings) {
            for (var j in del) {
                if (strings[i] == del[j]) {
                    continue top;
                }
            }
            unique.push(strings[i]);
        }
        $("#from-what-to-cut").val(unique.join("\r\n"));
    });
    // Link trimmer
    $("#find-links").click(function () {
        var strings = $("#text-with-links")
            .val()
            .split(/(https?:\/\/[^\s]+)/);
        var links = [];
        for (var i in strings) {
            if (strings[i].substr(0, 4) == "http") {
                links.push(strings[i]);
            }
        }
        $("#text-with-links").val(links.join("\r\n"));
    });
    // Weird reducer
    $("#convert-to-row").click(function () {
        var rows = $("#column-nums")
            .val()
            .split(/[\r\n]+/);
        for (var i in rows) {
            rows[i] -= 2000;
        }
        $("#column-nums").val(rows.join(";"));
    });
    // Word extractor
    $("#extract-words").click(function () {
        var tokens,
            rows = [];
        tokens = Az.Tokens(document.getElementById("semtext").value);
        var filtered = tokens.done();
        for (var i in filtered) {
            if (filtered[i].type === Az.Tokens.WORD && filtered[i].length > 2)
                rows.push(filtered[i]);
        }
        $("#semtext").val(rows.join("\r\n"));
    });
    // Row sum calculator
    $("#addup").click(function () {
        var rows = $("#nums-to-calculate")
            .val()
            .split(/[\r\n]+/);
        var sum = 0;
        for (var i in rows) {
            rows[i] = rows[i].replace(",", ".");
            rows[i] = parseFloat(rows[i]);
            sum += rows[i];
        }
        $("#nums-to-calculate").val(sum.toFixed(3));
    });
    // Row to array converter
    $("#rows-to-array-btn").click(function () {
        var rows = $("#rows-to-array-input")
            .val()
            .split(/[\r\n]+/);
        var arrayString = "[" + rows.map(row => `'${row.replace(/'/g, "\\'")}'`).join(", ") + "]";
        $("#rows-to-array-input").val(arrayString);
    });
    // Array to rows converter
    $("#array-to-rows-btn").click(function () {
        var rows = $("#rows-to-array-input")
            .val()
            .replace(/^\[|\]$/g, "")
            .replace(/\r?\n|\r/g, "")
            .split(/, ?/)
            .map(row => row.replace(/^'|'$/g, "").replace(/\\'/g, "'"));
        var arrayString = rows.join("\r\n");
        $("#rows-to-array-input").val(arrayString);
    });
});
