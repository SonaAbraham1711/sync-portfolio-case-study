{\rtf1\ansi\ansicpg1252\cocoartf2867
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 # app.py - Complete Sync Portfolio Case Study\
import streamlit as st\
import pandas as pd\
import plotly.express as px\
import plotly.graph_objects as go\
\
st.set_page_config(\
    page_title="Sync Product Case Study",\
    page_icon="\uc0\u55356 \u57263 ",\
    layout="wide"\
)\
\
# Custom CSS for professional portfolio layout\
st.markdown("""\
<style>\
    .hero \{\
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);\
        padding: 2rem;\
        border-radius: 20px;\
        color: white;\
        margin-bottom: 2rem;\
        text-align: center;\
    \}\
    .section-header \{\
        font-size: 1.8rem;\
        font-weight: 600;\
        color: #2563EB;\
        margin-top: 2rem;\
        margin-bottom: 1rem;\
        border-bottom: 2px solid #E5E7EB;\
        padding-bottom: 0.5rem;\
    \}\
    .metric-card \{\
        background: white;\
        padding: 1.5rem;\
        border-radius: 15px;\
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);\
        text-align: center;\
        border: 1px solid #E5E7EB;\
    \}\
</style>\
""", unsafe_allow_html=True)\
\
# Sidebar Navigation\
with st.sidebar:\
    st.title("\uc0\u55357 \u56522  Sync Case Study")\
    st.markdown("### Product Management Portfolio")\
    st.markdown("**Role:** Product Manager")\
    st.markdown("**Timeline:** 3-Month Project")\
    st.markdown("---")\
    \
    page = st.radio(\
        "Navigate",\
        [\
            "\uc0\u55356 \u57263  Problem",\
            "\uc0\u55357 \u56589  Research",\
            "\uc0\u55357 \u56481  Insights",\
            "\uc0\u55357 \u56960  Solution",\
            "\uc0\u55357 \u56520  Results",\
            "\uc0\u55356 \u57235  Learnings"\
        ]\
    )\
\
# HERO SECTION - Shows on all pages\
st.markdown("""\
<div class="hero">\
    <h1 style="color: white; border-bottom: none;">From Assumptions to Insights</h1>\
    <p style="font-size: 1.2rem; color: white;">Designing a User-Centric Feedback Process for Sync's Enterprise Clients</p>\
</div>\
""", unsafe_allow_html=True)\
\
# ============ PAGE 1: PROBLEM ============\
if page == "\uc0\u55356 \u57263  Problem":\
    st.title("\uc0\u55356 \u57263  The Silent Churn Problem")\
    \
    col1, col2 = st.columns([2, 1])\
    \
    with col1:\
        st.markdown("""\
        ### \uc0\u55357 \u57000  46% of Enterprise Revenue at Risk\
        \
        **Academic and Government clients**\'97contributing nearly half of Sync's enterprise revenue\'97\
        were quietly disengaging without providing feedback.\
        \
        **The Core Issue:**\
        - No feedback mechanism existed for enterprise users\
        - Security concerns forced manual workarounds\
        - Satisfaction score: **2/5** (vs Corporate: 4/5)\
        - Users actively researching competitor platforms\
        \
        > *"We have someone manually monitor every important meeting because we can't trust the permissions."*\
        > \'97 University IT Director\
        """)\
    \
    with col2:\
        st.metric("Revenue at Risk", "46%", "\uc0\u9888 \u65039  Critical")\
        st.metric("Satisfaction Score", "2.0/5.0", "-60% vs target")\
        st.metric("Silent Churn Rate", "15%", "Estimated")\
        st.metric("Users Using Workarounds", "83%", "From interviews")\
    \
    # Problem visualization\
    chart_data = pd.DataFrame(\{\
        'Segment': ['Government', 'Academic', 'Corporate', 'Startup'],\
        'Satisfaction': [2.0, 2.0, 4.0, 3.5],\
        'Revenue %': [33, 13, 54, 0]\
    \})\
    \
    st.subheader("\uc0\u55357 \u56522  Satisfaction vs Revenue Contribution")\
    col1, col2 = st.columns(2)\
    \
    with col1:\
        fig = px.bar(chart_data, x='Segment', y='Satisfaction', \
                     color='Segment', title='Satisfaction Scores by Segment')\
        st.plotly_chart(fig, use_container_width=True)\
    \
    with col2:\
        fig2 = px.pie(chart_data, values='Revenue %', names='Segment', \
                      title='Enterprise Revenue Distribution')\
        st.plotly_chart(fig2, use_container_width=True)\
    \
    st.caption("Figure 1: The segments paying the most are the least satisfied")\
\
# ============ PAGE 2: RESEARCH ============\
elif page == "\uc0\u55357 \u56589  Research":\
    st.title("\uc0\u55357 \u56589  Research & Discovery")\
    \
    st.markdown("""\
    ## Mixed-Methods Research Approach\
    \
    I led comprehensive research combining quantitative data analysis with qualitative user insights.\
    """)\
    \
    col1, col2, col3 = st.columns(3)\
    \
    with col1:\
        st.markdown("### \uc0\u55357 \u56522  Quantitative")\
        st.markdown("""\
        - **24 user interviews** (Gov/Academic)\
        - **2,500+ support tickets** analyzed\
        - **1M+ sessions** behavioral data\
        - **5 competitors** analyzed\
        """)\
    \
    with col2:\
        st.markdown("### \uc0\u55356 \u57252  Qualitative")\
        st.markdown("""\
        - **83%** use manual workarounds\
        - **100%** experienced security incidents\
        - **67%** researching alternatives\
        - **45min** average interview depth\
        """)\
    \
    with col3:\
        st.markdown("### \uc0\u55357 \u56593  Key Findings")\
        st.markdown("""\
        1. Enterprise: **70 bugs/month** (vs Free: 10)\
        2. Gov/Academic satisfaction: **2/5**\
        3. Revenue at risk: **46%**\
        4. Feedback rate: **5%**\
        """)\
    \
    # Bug visualization\
    bug_data = pd.DataFrame(\{\
        'Tier': ['Enterprise', 'High Cost', 'Low Cost', 'Free'],\
        'Bugs per Month': [70, 30, 12, 10]\
    \})\
    \
    fig = px.bar(bug_data, x='Tier', y='Bugs per Month',\
                 title='Bug Reports by Tier (Monthly Average)',\
                 color='Bugs per Month',\
                 color_continuous_scale='Reds')\
    st.plotly_chart(fig, use_container_width=True)\
    st.caption("Figure 2: Enterprise users experience 7x more bugs than free tier")\
\
# ============ PAGE 3: INSIGHTS ============\
elif page == "\uc0\u55357 \u56481  Insights":\
    st.title("\uc0\u55357 \u56481  Key Insights & Prioritization")\
    \
    st.markdown("""\
    ## From Data to Action: The 5 Core Insights\
    \
    After synthesizing 150+ data points, 5 critical insights emerged:\
    """)\
    \
    insights = [\
        ("1\uc0\u65039 \u8419  Poor Fit, Not Low Interest", \
         "Gov/Academic users show strong intent but friction holds them back",\
         "Revenue +20% YoY, Satisfaction -50%"),\
        \
        ("2\uc0\u65039 \u8419  Reliability Promise Broken", \
         "Highest-paying users experience most bugs",\
         "70 bugs/month Enterprise vs 10 Free"),\
        \
        ("3\uc0\u65039 \u8419  Broad but Shallow", \
         "Works for general use, fails for compliance workflows",\
         "100% report permission incidents"),\
        \
        ("4\uc0\u65039 \u8419  Silent Disengagement", \
         "Users work around instead of complain",\
         "5% feedback rate, 83% workarounds"),\
        \
        ("5\uc0\u65039 \u8419  Revenue Risk is NOW", \
         "46% of enterprise revenue from dissatisfied users",\
         "67% actively evaluating competitors")\
    ]\
    \
    for title, desc, evidence in insights:\
        st.markdown(f"""\
        <div style="background: #FEF3C7; padding: 1rem; border-radius: 10px; margin-bottom: 1rem; border-left: 5px solid #F59E0B;">\
            <h4 style="margin: 0;">\{title\}</h4>\
            <p>\{desc\}</p>\
            <small>\uc0\u55357 \u56522  \{evidence\}</small>\
        </div>\
        """, unsafe_allow_html=True)\
    \
    st.subheader("\uc0\u55356 \u57263  MoSCoW Prioritization")\
    \
    col1, col2 = st.columns(2)\
    \
    with col1:\
        st.markdown("""\
        **\uc0\u55357 \u56628  MUST HAVE (MVP)**\
        - Silent User Detection System\
        - Basic permission controls\
        - Admin feedback dashboard\
        \
        **\uc0\u55357 \u57313  SHOULD HAVE (Next)**\
        - Reliability improvements\
        - Advanced analytics\
        """)\
    \
    with col2:\
        st.markdown("""\
        **\uc0\u55357 \u57314  COULD HAVE (Future)**\
        - AI meeting summaries\
        - Custom compliance reports\
        \
        **\uc0\u9899  WON'T HAVE (Not now)**\
        - Video effects\
        - Social features\
        """)\
\
# ============ PAGE 4: SOLUTION ============\
elif page == "\uc0\u55357 \u56960  Solution":\
    st.title("\uc0\u55357 \u56960  Solution: Smart Passive Feedback System")\
    \
    st.markdown("""\
    <div style="background: #D1FAE5; padding: 1.5rem; border-radius: 15px; border-left: 6px solid #10B981; margin-bottom: 2rem;">\
        <h3 style="margin: 0; color: #065F46;">\uc0\u55356 \u57263  Core Insight</h3>\
        <p style="font-size: 1.2rem; margin-top: 0.5rem;">If users won't speak up, we need to listen to their behavior.</p>\
    </div>\
    """, unsafe_allow_html=True)\
    \
    col1, col2 = st.columns(2)\
    \
    with col1:\
        st.markdown("""\
        ### \uc0\u55356 \u57256  Key Features\
        \
        **1. Emoji Reaction Slider**  \
        Post-meeting 5-second rating (\uc0\u55357 \u56862  \u55357 \u56848  \u55357 \u56842 )\
        \
        **2. Feature-Level Tagging**  \
        Contextual feedback on specific features\
        \
        **3. Behavioral Signal Detection**  \
        AI detects frustration from actions\
        \
        **4. Admin Dashboard**  \
        Real-time satisfaction trends\
        """)\
    \
    with col2:\
        st.markdown("""\
        ### \uc0\u55357 \u56520  Success Metrics\
        \
        | Metric | Target |\
        |--------|--------|\
        | Feedback Rate | 5% \uc0\u8594  50%+ |\
        | Satisfaction | 2.0 \uc0\u8594  3.5 |\
        | Silent Churn | -40% |\
        | Adoption | 70% |\
        """)\
    \
    st.markdown("---")\
    st.subheader("\uc0\u55357 \u56580  Design Iterations")\
    \
    st.markdown("""\
    **What Didn't Work:**\
    - \uc0\u10060  In-meeting pop-ups (disruptive)\
    - \uc0\u10060  10-point scales (42% abandonment)\
    - \uc0\u10060  No opt-out (privacy concerns)\
    \
    **What We Learned:**\
    - \uc0\u9989  Post-meeting only\
    - \uc0\u9989  3-point emoji scale optimal\
    - \uc0\u9989  Privacy controls build trust\
    """)\
\
# ============ PAGE 5: RESULTS ============\
elif page == "\uc0\u55357 \u56520  Results":\
    st.title("\uc0\u55357 \u56520  Results & Impact")\
    \
    col1, col2 = st.columns(2)\
    \
    with col1:\
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)\
        st.metric("Satisfaction Score", "2.0 \uc0\u8594  4.2", "+110%")\
        st.markdown('</div>', unsafe_allow_html=True)\
        \
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)\
        st.metric("Feedback Rate", "5% \uc0\u8594  68%", "+1260%")\
        st.markdown('</div>', unsafe_allow_html=True)\
        \
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)\
        st.metric("Silent Churn", "15% \uc0\u8594  6%", "-60%")\
        st.markdown('</div>', unsafe_allow_html=True)\
    \
    with col2:\
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)\
        st.metric("Enterprise Renewal", "82% \uc0\u8594  94%", "+12%")\
        st.markdown('</div>', unsafe_allow_html=True)\
        \
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)\
        st.metric("Revenue Protected", "$4.2M", "Annual")\
        st.markdown('</div>', unsafe_allow_html=True)\
        \
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)\
        st.metric("Support Tickets", "Baseline \uc0\u8594  -60%", "Bug-related")\
        st.markdown('</div>', unsafe_allow_html=True)\
    \
    st.subheader("\uc0\u55357 \u56522  Before vs After")\
    \
    results_df = pd.DataFrame(\{\
        'Metric': ['Satisfaction', 'Feedback Rate', 'Silent Churn', 'Renewal Rate'],\
        'Before': [2.0, 5, 15, 82],\
        'After': [4.2, 68, 6, 94]\
    \})\
    \
    fig = px.bar(results_df, x='Metric', y=['Before', 'After'],\
                 barmode='group', title='Key Metrics: Before vs After',\
                 color_discrete_map=\{'Before': '#EF4444', 'After': '#10B981'\})\
    st.plotly_chart(fig, use_container_width=True)\
\
# ============ PAGE 6: LEARNINGS ============\
else:\
    st.title("\uc0\u55356 \u57235  Learnings & Conclusion")\
    \
    st.markdown("""\
    ## Key Takeaways\
    \
    This project taught me that the most critical user problems are often the quietest ones.\
    """)\
    \
    col1, col2 = st.columns(2)\
    \
    with col1:\
        st.markdown("""\
        ### \uc0\u9989  What Went Well\
        \
        1. **Problem Discovery** - Identified silent churn before it escalated\
        2. **Research Depth** - 24 interviews revealed workaround patterns\
        3. **Stakeholder Alignment** - Got CEO, CTO, Design on same page\
        4. **MVP Focus** - Shipped in 4 weeks, iterated based on feedback\
        5. **Measurable Impact** - Every metric improved significantly\
        """)\
    \
    with col2:\
        st.markdown("""\
        ### \uc0\u55357 \u56999  Challenges Overcome\
        \
        1. **Silent Users** - Shifted from surveys to behavioral signals\
        2. **Technical Debt** - Balanced new features with stability\
        3. **UX Concerns** - Proved passive feedback doesn't disrupt\
        4. **Privacy** - Built opt-out controls, increased adoption\
        5. **Cross-team Alignment** - Regular syncs prevented misalignment\
        """)\
    \
    st.markdown("---")\
    st.markdown("""\
    ### \uc0\u55357 \u56493  Final Reflection\
    \
    **The biggest lesson:** Users vote with their behavior, not their words. \
    \
    By building a system that listens to silent cues of dissatisfaction, we didn't just solve a feature gap\'97\
    we rebuilt trust with our most valuable clients.\
    \
    This project established a **data-driven feedback culture** at Sync that continues to inform product decisions today.\
    """)\
    \
    st.balloons()\
    st.success("\uc0\u9989  Case study complete! Thank you for reviewing my work.")\
\
# Footer\
st.markdown("---")\
st.markdown(\
    "<div style='text-align: center; color: #6B7280; padding: 1rem;'>"\
    "\uc0\u55357 \u56522  Sync Product Case Study | Product Management Portfolio | March 2024"\
    "</div>",\
    unsafe_allow_html=True\
)}