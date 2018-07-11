    $(function () {$("#start").click(function(){
var strings = $('#strings').val().split(/[\r\n]+/);var unique = [];top:for (var i in strings) {for (var j in unique) {if (strings[i] == unique[j]) {continue top;}}unique.push(strings[i]);}$('#strings').val(unique.join("\r\n"));});});

    $(function() {
        $("#start2").click(function() {
            var strings = $('#from-what-to-cut').val().split(/[\r\n]+/);
            var del = $('#what-to-cut').val().split(/[\r\n]+/);
            var unique = [];
            top: for (var i in strings) {
                for (var j in del) {
                    if (strings[i] == del[j]) {
                        continue top;
                    }
                }
                unique.push(strings[i]);
            }
            $('#from-what-to-cut').val(unique.join("\r\n"));
        });
        $("#findlinks").click(function() {
            var strings = $('#text-with-links').val().split(/(https?:\/\/[^\s]+)/);
            var links = [];
            for (var i in strings) {
                if (strings[i].substr(0,4) == "http") {
                    links.push(strings[i]);
                }
            }
            $('#text-with-links').val(links.join("\r\n"));
        });
        $("#convertToRow").click(function() {
            var rows = $('#column-nums').val().split(/[\r\n]+/);
            for (var i in rows) {
                rows[i] -= 2000;
            }
            $('#column-nums').val(rows.join(";"));
        });
        $("#semAnal").click(function() {
            var tokens, rows = [];
            tokens = Az.Tokens(document.getElementById('semtext').value);
            var filtered = tokens.done();
            for (var i in filtered) {
                if ((filtered[i].type === Az.Tokens.WORD) && (filtered[i].length > 2))
                    rows.push(filtered[i]);
            }
            $('#semtext').val(rows.join("\r\n"));
        });
    });
