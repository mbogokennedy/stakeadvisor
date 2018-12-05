let epl = document.getElementById("epl");
let fpl = document.getElementById("fpl");
let gpl = document.getElementById("gpl");
let ipl = document.getElementById("ipl");
let spl = document.getElementById("spl");
window.onload = function() {

    epl.style.display = "block";
    fpl.style.display = "none";
    gpl.style.display = "none";
    ipl.style.display = "none";
    spl.style.display = "none";
};

let btnfpl = document.getElementById("btn-fpl");
let btngpl = document.getElementById("btn-gpl");
let btnipl = document.getElementById("btn-ipl");
let btnspl = document.getElementById("btn-spl");
let btnepl = document.getElementById("btn-epl");

btnfpl.addEventListener('click', function() {
    epl.style.display = "none";
    fpl.style.display = "block";
    gpl.style.display = "none";
    ipl.style.display = "none";
    spl.style.display = "none";
});

btnepl.addEventListener('click', function() {
    epl.style.display = "block";
    fpl.style.display = "none";
    gpl.style.display = "none";
    ipl.style.display = "none";
    spl.style.display = "none";
});

btngpl.addEventListener('click', function() {
    epl.style.display = "none";
    fpl.style.display = "none";
    gpl.style.display = "block";
    ipl.style.display = "none";
    spl.style.display = "none";
});

btnipl.addEventListener('click', function() {
    epl.style.display = "none";
    fpl.style.display = "none";
    gpl.style.display = "none";
    ipl.style.display = "block";
    spl.style.display = "none";
});

btnspl.addEventListener('click', function() {
    epl.style.display = "none";
    fpl.style.display = "none";
    gpl.style.display = "none";
    ipl.style.display = "none";
    spl.style.display = "block";
});

try {
    function inscore_794082_xdc() {
        this.elm = null;
        this.hash = null;
        var times_resized = 0;
        var times_not_resized = 0;
        this.resize = function() {
            times_resized == 1023 && (times_resized = 0);
            times_not_resized == 1023 && (times_not_resized = 0);
            if (this.getElm() && location.hash && location.hash != this.hash) {
                this.hash = location.hash;
                var reggg = new RegExp(".*inscore_ifheight_xdc_([0-9]{2,5}).*");
                if (result = reggg.exec(location.hash)) {
                    this.getElm().style.height = (typeof result[1] == "undefined" ? "10000" : (result[1] > 500 && result[1] <= 50000 ? parseInt(result[1]) : 500)) + "px";
                    times_resized++;
                }
            } else if (location.hash && location.hash == this.hash) times_not_resized++;
            else return resize_later(75);
            resize_later(250);
        };
        var resize_later = function(time) {
            setTimeout(function() {
                inscore_794082_xdc_run.resize();
            }, time);
        };
        this.getElm = function() {
            try {
                (typeof this.elm == "undefined" || this.elm === null || !this.elm) && (this.elm = document.getElementById("inscore-xdc-794082"));
            } catch (e) {
                this.elm = null;
            }
            return this.elm;
        };
        var show_links = function() {
            if ((times_resized >= 1 || times_not_resized >= 2) && (obj = document.getElementById("freescore_links_794082"))) {
                obj.style.visibility = "none";
                obj.style.display = "none";
            } else show_links_later();
        };
        var show_links_later = function() {
            setTimeout(function() {
                show_links();
            }, 100);
        };
        if (typeof window.postMessage == "undefined") {
            show_links_later();
            resize_later();
        } else {
            var ev = function(event) {
                try {
                    var data = JSON.parse(event.data);
                } catch (e) {
                    return;
                }
                if (data instanceof Array && data[0] == 794082 && typeof data[1] != "undefined") {
                    eval(data[1]);
                }
            };
            if (window.addEventListener) {
                window.addEventListener("message", ev);
            } else if (window.attachEvent) {
                window.attachEvent("onmessage", ev);
            }
            setTimeout(function() {
                document.getElementById("inscore-xdc-794082").contentWindow.postMessage(JSON.stringify(["794082", "run"]), "*");
            }, 2000);
            show_links_later();
            resize_later();
        }
    };
    var inscore_794082_xdc_run = new inscore_794082_xdc();
} catch (e) {
    document.getElementById("inscore-xdc-794082").style.height = "10000px";
}