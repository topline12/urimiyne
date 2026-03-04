import streamlit as st
st.set_page_config(page_title="Kartoline per 7 mars")
st.subheader("Nje kartoline per ty")
urim_per_mesuesit={
    "Xheni":"Ju falenderojme per dijet qe na jepni ne teknologji",
    "Yllka":"Ju falenderojme per dijet qe na jepni ne biologji",
    "Gladiola":"Ju falenderojme per dijet qe na jepni ne anglisht",
    "Andi":"Ju falenderojme per dijet qe na jepni ne muzike",
    "Loreta":"Ju falenderojme per dijet qe na jepni ne gjeografi",
    "Laura":"Ju falenderojme per dijet qe na jepni ne matematike",
    "Rexhina":"Ju falenderojme per dijet qe na jepni ne fizike",
    "Albana Bega":"Ju falenderojme per drejtimin e shkolles ne nje menyre te drejte",
    "Albana Agalliu":"Ju falenderojme per mbeshtetjen dhe keshillat qe na jep",
    "Aibana":"Ju falenderojme per njohurite qe na jep ne frengjisht",
    "Majlinda":"Ju falenderojme per njohurite qe na jepni ne gjuhen shqipe",
    "Luli":"Ju falenderojme per njohurite qe na jepni ne biologji dhe kimi",
    "Genta":"Ju falenderojme per prezencen qe e ngrohte qe sjell ne shkolle",
    "Arta":"Oficere, ju falenderojme per kontrollin dhe mbeshtjen qe na jep",
    "Paçi":"Ju falenderojme per njohurite qe na jep ne biologji dhe kimi",
    "Andon":"Ju falenderojme per njohurite qe na jep ne art pamor",
    "Zeni":"Ju falenderojme per aktivitetet qe na zhvillon ne fiskulture",
    "Avenir":"Ju falenderojme per aktivitetet qe na zhvillon ne fiskulture",
    "Egla":"Ju falenderojme per njohurite qe na jepni ne gjuhe shqipe",
    "Erida":"Ju falenderojme per njohurite qe na jepni ne qytetari dhe gjuhe shqipe",
    "Vojsava":"Ju falenderojme per njohurite qe na jepni ne gjeografi dhe histori",
    "Liza":"Ju falenderojme per njohurite qe na jepni ne matematike dhe fizike",
    "Margarita":"Ju falenderojme per njohurite qe na jepni ne gjuhe shqipe",
    "Anila":"Ju falenderojme per njohurite qe na jepni ne gjeografi dhe histori",
}
emri=st.text_input("Vendosni emrin tuaj: ")
if st.button("Shfaq urimin 🌷"):
    if not emri:
        st.warning("Ju lutem plotesoni emrin tuaj")
    elif emri not in urim_per_mesuesit:
            st.error("Ky mesues nuk punon ne shkollen 22 Tetori")
    else:
        urimi_personal=urim_per_mesuesit[emri]
        st.markdown(f"""
        <div style="
             text-align:center;
             background: linear-gradient(135deg,
                 #d4edda, #e6f7e6);
             padding:20px;
             border-radius:20px;
             border:3px solid #28a745;
             font-size:20px;
             box-shadow:0 6px 15px rgba(0,0,0,0.15);
             ">
             <h4> GEZUAR FESTEN! </h4>  <br>
             <p> {urimi_personal} </p> <br>
             <p> Me dashuri nga Klubi I Kodimit </p>
             <p>Shkolla "22 Tetori" </p>
             </div>

             """, unsafe_allow_html=True)


