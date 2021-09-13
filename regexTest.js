
var sstr = "hello~~aa~~dw[aww]w**w**dawds__dwa__dwa"
var broken = "***This*** **is** _a_ *test* ___text___ __for__ ~~markdown~~"

function parseMarkdown(text){
    const pattern = /(\*{1,3}|_{1,3}|~~).+?\1/gm
    var res = text.replace(pattern,match=>{
        switch (true){
            case !!match.match(/(\*{1,3})(.*)\1/gm):
                var copy = match.match(/(\*{1,3})(.*)\1/).pop()
                switch (true){
                    case match.startsWith("***"):
                        return `<b><i>${copy}</i></b>`
                    case match.startsWith("**"):
                        return `<b>${copy}</b>`
                    case match.startsWith("*"):
                        return `<i>${copy}</i>`
                }
                break;
            case !!match.match(/(\_{1,3})(.*)\1/gm):
                var copy = match.match(/(\_{1,3})(.*)\1/).pop()
                switch (true){
                    case match.startsWith("___"):
                        return `<u><i>${copy}</i></u>`
                    case match.startsWith("__"):
                        return `<u>${copy}</u>`
                    case match.startsWith("_"):
                        return `<i>${copy}</i>`
                }
                break;
            case !!match.match(/(~{2})(.*)\1/gm):
                var copy = match.match(/(~{2})(.*)\1/).pop()
                return `<s>${copy}</s>`
        }
    })
    return res
}


console.log(parseMarkdown(broken))

