import streamlit as st
from pathlib import Path

# Build absolute base path
BASE = Path(__file__).parent / "outputs" / "figures"

st.set_page_config(
    page_title="Disease Outcome Survival Analysis",
    page_icon="📈",
    layout="wide"
)

st.title("📈 Disease Outcome Survival Analysis")
st.markdown(
    "Kaplan-Meier and Cox Proportional Hazards models estimating survival "
    "probabilities and interpreting clinical risk factors over time — "
    "applied to breast cancer recurrence-free survival data."
)

st.divider()

tab1, tab2, tab3, tab4 = st.tabs([
    "📊 Exploratory Analysis",
    "📉 Kaplan-Meier Curves",
    "🌲 Cox PH Model",
    "🎯 Predictions & Diagnostics"
])

with tab1:
    st.subheader("Exploratory Data Analysis")

    c1, c2 = st.columns(2)
    with c1:
        st.markdown("#### Event vs Censored Proportion")
        st.image(str(BASE / "Event_vs_Censored_Proportion.png"), use_column_width=True)
    with c2:
        st.markdown("#### Categorical Feature Event Rates")
        st.image(str(BASE / "Categorical_Feature_Event_Rates.png"), use_column_width=True)

    c3, c4 = st.columns(2)
    with c3:
        st.markdown("#### Numeric Feature Distributions by Outcome")
        st.image(str(BASE / "Numeric_Feature_Distributions_by_Outcome.png"), use_column_width=True)
    with c4:
        st.markdown("#### Pearson Correlation Matrix")
        st.image(str(BASE / "Pearson_Correlation_Matrix_Numeric_Features.png"), use_column_width=True)

    st.markdown("#### Effect of Log Transformation")
    st.image(str(BASE / "Effect_of_Log_Transformation.png"), use_column_width=True)

with tab2:
    st.subheader("Kaplan-Meier Survival Curves")

    st.markdown("#### Overall Kaplan-Meier Survival Curve")
    st.image(str(BASE / "Overall_Kaplan-Meier_Survival_Curve.png"), use_column_width=True)

    c1, c2 = st.columns(2)
    with c1:
        st.markdown("#### KM by Age Group")
        st.image(str(BASE / "KM_by_Age Group.png"), use_column_width=True)
    with c2:
        st.markdown("#### KM by Menopausal Status")
        st.image(str(BASE / "KM_by_Menopausal_Status.png"), use_column_width=True)

    c3, c4 = st.columns(2)
    with c3:
        st.markdown("#### KM by Tumour Grade")
        st.image(str(BASE / "KM_Survival_Curves_by_Tumour_Grade.png"), use_column_width=True)
    with c4:
        st.markdown("#### KM by Hormonal Therapy Status")
        st.image(str(BASE / "KM_Survival_Curves_by_Hormonal_Therapy_Status.png"), use_column_width=True)

    st.markdown("#### Recurrence-Free Survival Probability")
    st.image(str(BASE / "Recurrence-Free_Survival_Probability.png"), use_column_width=True)

with tab3:
    st.subheader("Cox Proportional Hazards Model")

    st.markdown("#### Forest Plot — Multivariable Cox PH Model")
    st.image(str(BASE / "Forest_Plot — Multivariable_Cox_PH_Model.png"), use_column_width=True)
    st.info(
        "The forest plot shows hazard ratios and 95% confidence intervals "
        "for each clinical covariate. Features with HR > 1 increase the "
        "hazard of recurrence; HR < 1 is protective."
    )

    c1, c2 = st.columns(2)
    with c1:
        st.markdown("#### Adjusted Survival by Tumour Grade")
        st.image(str(BASE / "Adjusted_Survival_by_Tumour_Grade.png"), use_column_width=True)
    with c2:
        st.markdown("#### Adjusted Survival by Hormonal Therapy")
        st.image(str(BASE / "Adjusted_Survival_by_Hormonal_Therapy.png"), use_column_width=True)

    st.markdown("#### Adjusted Survival by Number of Positive Lymph Nodes")
    st.image(str(BASE / "Adjusted_Survival_by_Number_of_Positive_Lymph_Nodes.png"), use_column_width=True)

    st.markdown("#### Model Discrimination — Concordance Index Comparison")
    st.image(str(BASE / "Model_Discrimination_Concordance_Index_Comparison.png"), use_column_width=True)

with tab4:
    st.subheader("Predictions & Model Diagnostics")

    st.markdown("#### Predicted Recurrence-Free Survival Probability")
    st.image(str(BASE / "Predicted_Recurrence-Free_Survival_Probability.png"), use_column_width=True)

    c1, c2 = st.columns(2)
    with c1:
        st.markdown("#### Proportional Hazards Visual Check")
        st.image(str(BASE / "Proportional_Hazards_Visual_Check.png"), use_column_width=True)
        st.info(
            "Schoenfeld residuals plotted over time to verify the "
            "proportional hazards assumption holds for each covariate."
        )
    with c2:
        st.markdown("#### Survival Analysis Summary")
        st.image(str(BASE / "survival_analysis_summary.png"), use_column_width=True)

st.divider()
st.caption(
    "Built by Stellamaries Syombua · "
    "Disease Outcome Survival Analysis · "
    "Models: Kaplan-Meier, Cox Proportional Hazards"
)
