#lexical diversity feauture extraction attempt
#based from this library: https://pypi.org/project/lexicalrichness/


from lexicalrichness import LexicalRichness

def TTR(article):

        text.lower()
        text.replace(".", " ")
        text.replace("!", " ")
        text.replace("?", " ")
        text.replace(":", " ")
        text.replace(";", " ")
        text.replace("\"", " ")
        text.replace("/", " ")
        text.replace("#", " ")
        text.replace("$", " ")
        text.replace("*", " ")
        text.replace("@", " ")
        text.replace("(", " ")
        text.replace(")", " ")
        text.replace(",", " ")
        text.replace("[", " ")
        text.replace("]", " ")

        lex = LexicalRichness(text)
        ttr = lex.ttr #type token ratio
        rttr = lex.rttr #root type token ratio
        cttr = lex.cttr #corrected ttr
        msttr = lex.msttr(segment_window=25) #mean segmental ttr
        mtld = lex.mtld(threshold=0.72) #Measure of Textual Lexical Diversity
        hdd = lex.hdd(draws=42)#hypergeometric distribution diversity
        
        return text, ttr, rttr, cttr, msttr, mtld, hdd

