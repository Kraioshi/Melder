import streamlit as st
from PIL import Image

st.set_page_config("OmegaMelder", layout="wide")

s_head = Image.open("s_head.png")
s_weapon = Image.open("s_weapon.png")
s_body = Image.open("s_body.png")
s_hands = Image.open("s_hands.png")
s_pants = Image.open("s_pants.png")
s_boots = Image.open("s_boots.png")
s_ears = Image.open("s_ears.png")
s_neck = Image.open("s_neck.png")
s_bracelets = Image.open("s_bracelets.png")
s_ring_tome = Image.open("s_ring_tome.png")
s_ring_raid = Image.open("s_ring_raid.png")
s_food = Image.open("s_carrot.png")
tome = Image.open("causality.png")
book1 = Image.open("book1.png")
book2 = Image.open("book2.png")
book4 = Image.open("book4.png")
pudding = Image.open("s_carrot.png")
pizza = Image.open("s_pizza.png")


DH = "Heavens' Eye Materia X"
CRIT = "Savage Aim Materia X"
DET = "Savage Might Materia X"
SPS = "Quicktongue Materia X"


col1, col2, col3, col4, col5, col6, col7 = st.columns(7)

with col1:
    st.subheader("Select job")
    smn = st.checkbox("Summoner")
    rdm = st.checkbox("Red Mage")


with col2:
    if smn:
        st.subheader("SMN builds")
        st.markdown("**Crit Builds**")
        two_48 = st.button("2.48", key="smn248")
        two_47 = st.button("2.47")
        two_46 = st.button("2.46")
        two_45 = st.button("2.45")
        st.markdown("**SPS Builds**")
        two_19 = st.button("2.19")
        two_18 = st.button("2.18")
# 2.48 build
        if two_48:
            with col3:                                                                                          # weapon
                st.subheader("2.48 GCD")
                st.markdown("**List of items**")
                st.caption("")
                st.image(s_weapon, width=67)
                st.markdown("***")
                with col4:
                    st.subheader("Melds")
                    st.markdown("**Meld only X materia**")
                    st.text("")
                    st.markdown("Direct Hit Rate +36")
                    st.markdown("Direct Hit Rate +36")
                    st.markdown("***")
                    with col5:
                        st.subheader("Materia")
                        st.markdown("**DHit / Crit / Det**")
                        st.markdown("")
                        st.markdown(DH)
                        st.markdown(DH)
                        st.markdown("***")
                        with col6:
                            st.subheader("Source")
                            st.markdown("**Raid / Tome**")
                            st.markdown("")
                            st.image(book4, width=67)
                            st.markdown("---")
                            with col7:
                                st.subheader("Food")
                                st.markdown("**Carrot Pudding**")
                                st.markdown("")
                                st.image(pudding, width=67)
                                st.markdown("---")

                st.image(s_head, width=68)                                                              # head
                st.markdown("***")
                with col4:
                    st.markdown("Direct Hit Rate +36")
                    st.markdown("Direct Hit Rate +36")
                    st.markdown("---")
                    with col5:
                        st.markdown(DH)
                        st.markdown(DH)
                        st.markdown("---")
                        with col6:
                            st.image(tome, width=68)
                            st.markdown("---")

                st.image(s_body, width=67)                                                               # body
                st.markdown("---")
                with col4:
                    st.markdown("Direct Hit Rate +36")
                    st.markdown("Direct Hit Rate +36")
                    st.markdown("---")
                    with col5:
                        st.markdown(DH)
                        st.markdown(DH)
                        st.markdown("---")
                        with col6:
                            st.image(book4, width=67)
                            st.markdown("---")

                st.image(s_hands, width=67)                                                               # hands
                st.markdown("---")
                with col4:
                    st.markdown("Direct Hit Rate +36")
                    st.markdown("Direct Hit Rate +36")
                    st.markdown("---")
                    with col5:
                        st.markdown(DH)
                        st.markdown(DH)
                        st.markdown("---")
                        with col6:
                            st.image(book2, width=67)
                            st.markdown("---")

                st.image(s_pants, width=67)                                                             # pants
                st.markdown("---")
                with col4:
                    st.markdown("Direct Hit Rate +36")
                    st.markdown("Direct Hit Rate +36")
                    st.markdown("---")
                    with col5:
                        st.markdown(DH)
                        st.markdown(DH)
                        st.markdown("---")
                        with col6:
                            st.image(tome, width=67)
                            st.markdown("---")

                st.image(s_boots, width=67)                                                             # boots
                st.markdown("---")
                with col4:
                    st.markdown("Determination +36")
                    st.markdown("Critical Hit Rate +36")
                    st.markdown("---")
                    with col5:
                        st.markdown(DET)
                        st.markdown(CRIT)
                        st.markdown("---")
                        with col6:
                            st.image(tome, width=67)
                            st.markdown("---")

                st.image(s_ears, width=67)                                                             # ears
                st.markdown("---")
                with col4:
                    st.markdown("Direct Hit Rate +36")
                    st.markdown("Critical Hit Rate +36")
                    st.markdown("---")
                    with col5:
                        st.markdown(DH)
                        st.markdown(CRIT)
                        st.markdown("---")
                        with col6:
                            st.image(book1, width=67)
                            st.markdown("---")

                st.image(s_neck, width=68)                                                             # neck
                st.markdown("---")
                with col4:
                    st.markdown("Direct Hit Rate +36")
                    st.markdown("Critical Hit Rate +36")
                    st.markdown("---")
                    with col5:
                        st.markdown(DH)
                        st.markdown(CRIT)
                        st.markdown("---")
                        with col6:
                            st.image(tome, width=68)
                            st.markdown("---")

                st.image(s_bracelets, width=67)                                                             # bracelets
                st.markdown("---")
                with col4:
                    st.markdown("Determination +36")
                    st.markdown("Direct Hit Rate +36")
                    st.markdown("---")
                    with col5:
                        st.markdown(DET)
                        st.markdown(DH)
                        st.markdown("---")
                        with col6:
                            st.image(book1, width=67)
                            st.markdown("---")

                st.image(s_ring_tome, width=67)                                                             # ring_tome
                st.markdown("---")
                with col4:
                    st.markdown("Critical Hit Rate +36")
                    st.markdown("Critical Hit Rate +36")
                    st.markdown("---")
                    with col5:
                        st.markdown(CRIT)
                        st.markdown(CRIT)
                        st.markdown("---")
                        with col6:
                            st.image(tome, width=67)
                            st.markdown("---")

                st.image(s_ring_raid, width=67)                                                             # ring_raid
                st.markdown("---")
                with col4:
                    st.markdown("Direct Hit Rate +36")
                    st.markdown("Direct Hit Rate +36")
                    st.markdown("---")
                    with col5:
                        st.markdown(DH)
                        st.markdown(DH)
                        st.markdown("---")
                        with col6:
                            st.image(tome, width=67)
                            st.markdown("---")

# 2.47 build
        elif two_47:
            with col3:                                                                                          # weapon
                st.subheader("2.48 GCD")
                st.markdown("**List of items**")
                st.caption("")
                st.image(s_weapon, width=67)
                st.markdown("***")
                with col4:
                    st.subheader("Melds")
                    st.markdown("**Meld only X materia**")
                    st.text("")
                    st.markdown("Direct Hit Rate +36")
                    st.markdown("Direct Hit Rate +36")
                    st.markdown("***")
                    with col5:
                        st.subheader("Materia")
                        st.markdown("**DHit / Crit / Det**")
                        st.markdown("")
                        st.markdown(DH)
                        st.markdown(DH)
                        st.markdown("***")
                        with col6:
                            st.subheader("Source")
                            st.markdown("**Raid / Tome**")
                            st.markdown("")
                            st.image(book4, width=67)
                            st.markdown("---")
                            with col7:
                                st.subheader("Food")
                                st.markdown("**Carrot Pudding**")
                                st.markdown("")
                                st.image(pizza, width=67)
                                st.markdown("---")

                st.image(s_head, width=68)                                                              # head
                st.markdown("***")
                with col4:
                    st.markdown("Direct Hit Rate +36")
                    st.markdown("Direct Hit Rate +36")
                    st.markdown("---")
                    with col5:
                        st.markdown(DH)
                        st.markdown(DH)
                        st.markdown("---")
                        with col6:
                            st.image(tome, width=68)
                            st.markdown("---")

                st.image(s_body, width=67)                                                               # body
                st.markdown("---")
                with col4:
                    st.markdown("Direct Hit Rate +36")
                    st.markdown("Direct Hit Rate +36")
                    st.markdown("---")
                    with col5:
                        st.markdown(DH)
                        st.markdown(DH)
                        st.markdown("---")
                        with col6:
                            st.image(book4, width=67)
                            st.markdown("---")

                st.image(s_hands, width=67)                                                               # hands
                st.markdown("---")
                with col4:
                    st.markdown("Direct Hit Rate +36")
                    st.markdown("Direct Hit Rate +36")
                    st.markdown("---")
                    with col5:
                        st.markdown(DH)
                        st.markdown(DH)
                        st.markdown("---")
                        with col6:
                            st.image(book2, width=67)
                            st.markdown("---")

                st.image(s_pants, width=67)                                                             # pants
                st.markdown("---")
                with col4:
                    st.markdown("Direct Hit Rate +36")
                    st.markdown("Direct Hit Rate +36")
                    st.markdown("---")
                    with col5:
                        st.markdown(DH)
                        st.markdown(DH)
                        st.markdown("---")
                        with col6:
                            st.image(tome, width=67)
                            st.markdown("---")

                st.image(s_boots, width=67)                                                             # boots
                st.markdown("---")
                with col4:
                    st.markdown("Determination +36")
                    st.markdown("Critical Hit Rate +36")
                    st.markdown("---")
                    with col5:
                        st.markdown(DET)
                        st.markdown(CRIT)
                        st.markdown("---")
                        with col6:
                            st.image(tome, width=67)
                            st.markdown("---")

                st.image(s_ears, width=67)                                                             # ears
                st.markdown("---")
                with col4:
                    st.markdown("Direct Hit Rate +36")
                    st.markdown("Critical Hit Rate +36")
                    st.markdown("---")
                    with col5:
                        st.markdown(DH)
                        st.markdown(CRIT)
                        st.markdown("---")
                        with col6:
                            st.image(book1, width=67)
                            st.markdown("---")

                st.image(s_neck, width=68)                                                             # neck
                st.markdown("---")
                with col4:
                    st.markdown("Direct Hit Rate +36")
                    st.markdown("Critical Hit Rate +36")
                    st.markdown("---")
                    with col5:
                        st.markdown(DH)
                        st.markdown(CRIT)
                        st.markdown("---")
                        with col6:
                            st.image(tome, width=68)
                            st.markdown("---")

                st.image(s_bracelets, width=67)                                                             # bracelets
                st.markdown("---")
                with col4:
                    st.markdown("Determination +36")
                    st.markdown("Direct Hit Rate +36")
                    st.markdown("---")
                    with col5:
                        st.markdown(DET)
                        st.markdown(DH)
                        st.markdown("---")
                        with col6:
                            st.image(book1, width=67)
                            st.markdown("---")

                st.image(s_ring_tome, width=67)                                                             # ring_tome
                st.markdown("---")
                with col4:
                    st.markdown("Critical Hit Rate +36")
                    st.markdown("Critical Hit Rate +36")
                    st.markdown("---")
                    with col5:
                        st.markdown(CRIT)
                        st.markdown(CRIT)
                        st.markdown("---")
                        with col6:
                            st.image(tome, width=67)
                            st.markdown("---")

                st.image(s_ring_raid, width=67)                                                             # ring_raid
                st.markdown("---")
                with col4:
                    st.markdown("Direct Hit Rate +36")
                    st.markdown("Direct Hit Rate +36")
                    st.markdown("---")
                    with col5:
                        st.markdown(DH)
                        st.markdown(DH)
                        st.markdown("---")
                        with col6:
                            st.image(tome, width=67)
                            st.markdown("---")

# 2.46 build
        if two_46:
            with col3:                                                                                          # weapon
                st.subheader("2.48 GCD")
                st.markdown("**List of items**")
                st.caption("")
                st.image(s_weapon, width=67)
                st.markdown("***")
                with col4:
                    st.subheader("Melds")
                    st.markdown("**Meld only X materia**")
                    st.text("")
                    st.markdown("Direct Hit Rate +36")
                    st.markdown("Direct Hit Rate +36")
                    st.markdown("***")
                    with col5:
                        st.subheader("Materia")
                        st.markdown("**DHit / Crit / Det**")
                        st.markdown("")
                        st.markdown(DH)
                        st.markdown(DH)
                        st.markdown("***")
                        with col6:
                            st.subheader("Source")
                            st.markdown("**Raid / Tome**")
                            st.markdown("")
                            st.image(book4, width=67)
                            st.markdown("---")
                            with col7:
                                st.subheader("Food")
                                st.markdown("**Carrot Pudding**")
                                st.markdown("")
                                st.image(pudding, width=67)
                                st.markdown("---")

                st.image(s_head, width=68)                                                              # head
                st.markdown("***")
                with col4:
                    st.markdown("Direct Hit Rate +36")
                    st.markdown("Direct Hit Rate +36")
                    st.markdown("---")
                    with col5:
                        st.markdown(DH)
                        st.markdown(DH)
                        st.markdown("---")
                        with col6:
                            st.image(tome, width=68)
                            st.markdown("---")

                st.image(s_body, width=67)                                                               # body
                st.markdown("---")
                with col4:
                    st.markdown("Direct Hit Rate +36")
                    st.markdown("Direct Hit Rate +36")
                    st.markdown("---")
                    with col5:
                        st.markdown(DH)
                        st.markdown(DH)
                        st.markdown("---")
                        with col6:
                            st.image(book4, width=67)
                            st.markdown("---")

                st.image(s_hands, width=67)                                                               # hands
                st.markdown("---")
                with col4:
                    st.markdown("Direct Hit Rate +36")
                    st.markdown("Direct Hit Rate +36")
                    st.markdown("---")
                    with col5:
                        st.markdown(DH)
                        st.markdown(DH)
                        st.markdown("---")
                        with col6:
                            st.image(book2, width=67)
                            st.markdown("---")

                st.image(s_pants, width=67)                                                             # pants
                st.markdown("---")
                with col4:
                    st.markdown("Direct Hit Rate +36")
                    st.markdown("Direct Hit Rate +36")
                    st.markdown("---")
                    with col5:
                        st.markdown(DH)
                        st.markdown(DH)
                        st.markdown("---")
                        with col6:
                            st.image(tome, width=67)
                            st.markdown("---")

                st.image(s_boots, width=67)                                                             # boots
                st.markdown("---")
                with col4:
                    st.markdown("Spell Speed +36")
                    st.markdown("Critical Hit Rate +36")
                    st.markdown("---")
                    with col5:
                        st.markdown(SPS)
                        st.markdown(CRIT)
                        st.markdown("---")
                        with col6:
                            st.image(tome, width=67)
                            st.markdown("---")

                st.image(s_ears, width=67)                                                             # ears
                st.markdown("---")
                with col4:
                    st.markdown("Direct Hit Rate +36")
                    st.markdown("Critical Hit Rate +36")
                    st.markdown("---")
                    with col5:
                        st.markdown(DH)
                        st.markdown(CRIT)
                        st.markdown("---")
                        with col6:
                            st.image(book1, width=67)
                            st.markdown("---")

                st.image(s_neck, width=68)                                                             # neck
                st.markdown("---")
                with col4:
                    st.markdown("Direct Hit Rate +36")
                    st.markdown("Critical Hit Rate +36")
                    st.markdown("---")
                    with col5:
                        st.markdown(DH)
                        st.markdown(CRIT)
                        st.markdown("---")
                        with col6:
                            st.image(tome, width=68)
                            st.markdown("---")

                st.image(s_bracelets, width=67)                                                             # bracelets
                st.markdown("---")
                with col4:
                    st.markdown("Spell Speed +36")
                    st.markdown("Spell Speed +36")
                    st.markdown("---")
                    with col5:
                        st.markdown(SPS)
                        st.markdown(SPS)
                        st.markdown("---")
                        with col6:
                            st.image(book1, width=67)
                            st.markdown("---")

                st.image(s_ring_tome, width=67)                                                             # ring_tome
                st.markdown("---")
                with col4:
                    st.markdown("Critical Hit Rate +36")
                    st.markdown("Critical Hit Rate +36")
                    st.markdown("---")
                    with col5:
                        st.markdown(CRIT)
                        st.markdown(CRIT)
                        st.markdown("---")
                        with col6:
                            st.image(tome, width=67)
                            st.markdown("---")

                st.image(s_ring_raid, width=67)                                                             # ring_raid
                st.markdown("---")
                with col4:
                    st.markdown("Direct Hit Rate +36")
                    st.markdown("Direct Hit Rate +36")
                    st.markdown("---")
                    with col5:
                        st.markdown(DH)
                        st.markdown(DH)
                        st.markdown("---")
                        with col6:
                            st.image(tome, width=67)
                            st.markdown("---")

# 2.45 build
        if two_45:
            with col3:                                                                                          # weapon
                st.subheader("2.48 GCD")
                st.markdown("**List of items**")
                st.caption("")
                st.image(s_weapon, width=67)
                st.markdown("***")
                with col4:
                    st.subheader("Melds")
                    st.markdown("**Meld only X materia**")
                    st.text("")
                    st.markdown("Direct Hit Rate +36")
                    st.markdown("Direct Hit Rate +36")
                    st.markdown("***")
                    with col5:
                        st.subheader("Materia")
                        st.markdown("**DHit / Crit / Det**")
                        st.markdown("")
                        st.markdown(DH)
                        st.markdown(DH)
                        st.markdown("***")
                        with col6:
                            st.subheader("Source")
                            st.markdown("**Raid / Tome**")
                            st.markdown("")
                            st.image(book4, width=67)
                            st.markdown("---")
                            with col7:
                                st.subheader("Food")
                                st.markdown("**Carrot Pudding**")
                                st.markdown("")
                                st.image(pizza, width=67)
                                st.markdown("---")

                st.image(s_head, width=68)                                                              # head
                st.markdown("***")
                with col4:
                    st.markdown("Direct Hit Rate +36")
                    st.markdown("Direct Hit Rate +36")
                    st.markdown("---")
                    with col5:
                        st.markdown(DH)
                        st.markdown(DH)
                        st.markdown("---")
                        with col6:
                            st.image(tome, width=68)
                            st.markdown("---")

                st.image(s_body, width=67)                                                               # body
                st.markdown("---")
                with col4:
                    st.markdown("Direct Hit Rate +36")
                    st.markdown("Direct Hit Rate +36")
                    st.markdown("---")
                    with col5:
                        st.markdown(DH)
                        st.markdown(DH)
                        st.markdown("---")
                        with col6:
                            st.image(book4, width=67)
                            st.markdown("---")

                st.image(s_hands, width=67)                                                               # hands
                st.markdown("---")
                with col4:
                    st.markdown("Direct Hit Rate +36")
                    st.markdown("Direct Hit Rate +36")
                    st.markdown("---")
                    with col5:
                        st.markdown(DH)
                        st.markdown(DH)
                        st.markdown("---")
                        with col6:
                            st.image(book2, width=67)
                            st.markdown("---")

                st.image(s_pants, width=67)                                                             # pants
                st.markdown("---")
                with col4:
                    st.markdown("Direct Hit Rate +36")
                    st.markdown("Direct Hit Rate +36")
                    st.markdown("---")
                    with col5:
                        st.markdown(DH)
                        st.markdown(DH)
                        st.markdown("---")
                        with col6:
                            st.image(tome, width=67)
                            st.markdown("---")

                st.image(s_boots, width=67)                                                             # boots
                st.markdown("---")
                with col4:
                    st.markdown("Spell Speed +36")
                    st.markdown("Critical Hit Rate +36")
                    st.markdown("---")
                    with col5:
                        st.markdown(SPS)
                        st.markdown(CRIT)
                        st.markdown("---")
                        with col6:
                            st.image(tome, width=67)
                            st.markdown("---")

                st.image(s_ears, width=67)                                                             # ears
                st.markdown("---")
                with col4:
                    st.markdown("Direct Hit Rate +36")
                    st.markdown("Critical Hit Rate +36")
                    st.markdown("---")
                    with col5:
                        st.markdown(DH)
                        st.markdown(CRIT)
                        st.markdown("---")
                        with col6:
                            st.image(book1, width=67)
                            st.markdown("---")

                st.image(s_neck, width=68)                                                             # neck
                st.markdown("---")
                with col4:
                    st.markdown("Direct Hit Rate +36")
                    st.markdown("Critical Hit Rate +36")
                    st.markdown("---")
                    with col5:
                        st.markdown(DH)
                        st.markdown(CRIT)
                        st.markdown("---")
                        with col6:
                            st.image(tome, width=68)
                            st.markdown("---")

                st.image(s_bracelets, width=67)                                                             # bracelets
                st.markdown("---")
                with col4:
                    st.markdown("Spell Speed +36")
                    st.markdown("Spell Speed +36")
                    st.markdown("---")
                    with col5:
                        st.markdown(SPS)
                        st.markdown(SPS)
                        st.markdown("---")
                        with col6:
                            st.image(book1, width=67)
                            st.markdown("---")

                st.image(s_ring_tome, width=67)                                                             # ring_tome
                st.markdown("---")
                with col4:
                    st.markdown("Critical Hit Rate +36")
                    st.markdown("Critical Hit Rate +36")
                    st.markdown("---")
                    with col5:
                        st.markdown(CRIT)
                        st.markdown(CRIT)
                        st.markdown("---")
                        with col6:
                            st.image(tome, width=67)
                            st.markdown("---")

                st.image(s_ring_raid, width=67)                                                             # ring_raid
                st.markdown("---")
                with col4:
                    st.markdown("Direct Hit Rate +36")
                    st.markdown("Direct Hit Rate +36")
                    st.markdown("---")
                    with col5:
                        st.markdown(DH)
                        st.markdown(DH)
                        st.markdown("---")
                        with col6:
                            st.image(tome, width=67)
                            st.markdown("---")

    if rdm:
        st.subheader("RDM builds:")
        two_forty_eight = st.button("2.48")
        if two_forty_eight:
            with col3:
                st.subheader("2.48 GCD")
                st.text("Coming Soon :smile:")



