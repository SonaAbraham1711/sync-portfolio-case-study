# app.py - Sync Portfolio Case Study
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


st.set_page_config(
    page_title="Sync Product Case Study",
    page_icon="🎯",
    layout="wide"
)


# Custom CSS for professional layout
st.markdown("""
<style>
    .hero {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 20px;
        color: white;
        margin-bottom: 2rem;
        text-align: center;
    }
    .section-header {
        font-size: 1.8rem;
        font-weight: 600;
        color: #2563EB;
        margin-top: 2rem;
        margin-bottom: 1rem;
        border-bottom: 2px solid #E5E7EB;
        padding-bottom: 0.5rem;
    }
    .metric-card {
        background: white;
        padding: 1.5rem;
        border-radius: 15px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        text-align: center;
        border: 1px solid #E5E7EB;
    }
    .insight-card {
        background: #FEF3C7;
        padding: 1.2rem;
        border-radius: 10px;
        border-left: 5px solid #F59E0B;
        margin-bottom: 1rem;
    }
    .solution-card {
        background: #D1FAE5;
        padding: 1.2rem;
        border-radius: 10px;
        border-left: 5px solid #10B981;
        margin-bottom: 1rem;
    }
</style>
""", unsafe_allow_html=True)


# Sidebar Navigation
with st.sidebar:
    st.title("📊 Sync Case Study")
    st.markdown("### Product Management Portfolio")
    st.markdown("**Role:** Product Manager")
    st.markdown("**Timeline:** 3-Month Project")
    st.markdown("---")
    
    page = st.radio(
        "Navigate",
        ["🎯 Problem", "🔍 Research", "💡 Insights", "🚀 Solution", "📈 Results", "🎓 Learnings"]
    )


# Hero Section
st.markdown("""
<div class="hero">
    <h1 style="color: white; border-bottom: none;">From Assumptions to Insights</h1>
    <p style="font-size: 1.2rem; color: white;">Designing a User-Centric Feedback Process for Sync's Enterprise Clients</p>
</div>
""", unsafe_allow_html=True)


# ============ PAGE 1: PROBLEM ============
if page == "🎯 Problem":
    st.title("🎯 The Silent Churn Problem")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        ### 🚨 46% of Enterprise Revenue at Risk
        
        **Academic and Government clients**—contributing nearly half of Sync's enterprise revenue—
        were quietly disengaging without providing feedback.
        
        **The Core Issue:**
        - No feedback mechanism existed for enterprise users
        - Security concerns forced manual workarounds
        - Satisfaction score: **2/5** (vs Corporate: 4/5)
        - Users actively researching competitor platforms
        
        > *"We have someone manually monitor every important meeting because we can't trust the permissions."*
        > — University IT Director
        """)
    
    with col2:
        st.metric("Revenue at Risk", "46%", "⚠️ Critical")
        st.metric("Satisfaction Score", "2.0/5.0", "-60% vs target")
        st.metric("Silent Churn Rate", "15%", "Estimated")
        st.metric("Users Using Workarounds", "83%", "From interviews")
    
    # Visualization
    df1 = pd.DataFrame({
        'Segment': ['Government', 'Academic', 'Corporate', 'Startup'],
        'Satisfaction': [2.0, 2.0, 4.0, 3.5],
        'Revenue': [33, 13, 54, 0]
    })
    
    col1, col2 = st.columns(2)
    with col1:
        fig = px.bar(df1, x='Segment', y='Satisfaction', 
                     title='Satisfaction Scores by Segment',
                     color='Segment',
                     color_discrete_map={'Government':'#EF4444','Academic':'#EF4444',
                                       'Corporate':'#10B981','Startup':'#3B82F6'})
        st.plotly_chart(fig, use_container_width=True)
    with col2:
        fig2 = px.pie(df1, values='Revenue', names='Segment', 
                     title='Enterprise Revenue Distribution',
                     color_discrete_map={'Government':'#EF4444','Academic':'#F59E0B',
                                       'Corporate':'#10B981','Startup':'#3B82F6'})
        st.plotly_chart(fig2, use_container_width=True)
    
    st.caption("Figure 1: The segments paying the most are the least satisfied")


# ============ PAGE 2: RESEARCH ============
elif page == "🔍 Research":
    st.title("🔍 Research & Discovery")
    
    st.markdown("""
    ## Mixed-Methods Research Approach
    
    I led comprehensive research combining quantitative data analysis with qualitative user insights.
    """)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("### 📊 Quantitative")
        st.markdown("""
        - **2,500+** support tickets analyzed
        - **1M+** sessions behavioral data
        - **5** competitors analyzed
        - **70** bugs/month in Enterprise
        """)
    
    with col2:
        st.markdown("### 🎤 Qualitative")
        st.markdown("""
        - **24** user interviews
        - **83%** use manual workarounds
        - **100%** experienced security incidents
        - **67%** researching alternatives
        """)
    
    with col3:
        st.markdown("### 🔑 Key Findings")
        st.markdown("""
        1. Enterprise: **70 bugs/month** (vs Free: 10)
        2. Gov/Academic satisfaction: **2/5**
        3. Revenue at risk: **46%**
        4. Feedback rate: **5%**
        """)
    
    # Bug visualization
    df_bugs = pd.DataFrame({
        'Tier': ['Enterprise', 'High Cost', 'Low Cost', 'Free'],
        'Bugs per Month': [70, 30, 12, 10]
    })
    
    fig = px.bar(df_bugs, x='Tier', y='Bugs per Month',
                 title='Bug Reports by Tier (Monthly Average)',
                 color='Bugs per Month',
                 color_continuous_scale='Reds')
    st.plotly_chart(fig, use_container_width=True)
    st.caption("Figure 2: Enterprise users experience 7x more bugs than free tier")


# ============ PAGE 3: INSIGHTS ============
elif page == "💡 Insights":
    st.title("💡 Key Insights & Prioritization")
    
    st.markdown("## The 5 Core Insights")
    
    insights = [
        ("1. Poor Fit, Not Low Interest", 
         "Gov/Academic users show strong intent but friction holds them back",
         "Revenue +20% YoY, Satisfaction -50%"),
        
        ("2. Reliability Promise Broken", 
         "Highest-paying users experience most bugs",
         "70 bugs/month Enterprise vs 10 Free"),
        
        ("3. Broad but Shallow", 
         "Works for general use, fails for compliance workflows",
         "100% report permission incidents"),
        
        ("4. Silent Disengagement", 
         "Users work around instead of complain",
         "5% feedback rate, 83% workarounds"),
        
        ("5. Revenue Risk is NOW", 
         "46% of enterprise revenue from dissatisfied users",
         "67% actively evaluating competitors")
    ]
    
    for title, desc, evidence in insights:
        st.markdown(f"""
        <div class="insight-card">
            <h4 style="margin: 0;">{title}</h4>
            <p>{desc}</p>
            <small>📊 {evidence}</small>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("## 🎯 MoSCoW Prioritization")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **🔴 MUST HAVE (MVP)**
        - Silent User Detection System
        - Basic permission controls
        - Admin feedback dashboard
        
        **🟡 SHOULD HAVE (Next)**
        - Reliability improvements
        - Advanced analytics
        """)
    
    with col2:
        st.markdown("""
        **🟢 COULD HAVE (Future)**
        - AI meeting summaries
        - Custom compliance reports
        
        **⚫ WON'T HAVE (Not now)**
        - Video effects
        - Social features
        """)


# ============ PAGE 4: SOLUTION ============
elif page == "🚀 Solution":
    st.title("🚀 Solution: Smart Passive Feedback System")
    
    st.markdown("""
    <div class="solution-card">
        <h3 style="margin: 0; color: #065F46;">🎯 Core Insight</h3>
        <p style="font-size: 1.2rem; margin-top: 0.5rem;">If users won't speak up, we need to listen to their behavior.</p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### 🎨 Key Features
        
        **1. Emoji Reaction Slider**  
        Post-meeting 5-second rating (😞 😐 😊)
        
        **2. Feature-Level Tagging**  
        Contextual feedback on specific features
        
        **3. Behavioral Signal Detection**  
        AI detects frustration from actions
        
        **4. Admin Dashboard**  
        Real-time satisfaction trends
        """)
    
    with col2:
        st.markdown("""
        ### 📈 Success Metrics
        
        | Metric | Target |
        |--------|--------|
        | Feedback Rate | 5% → 50%+ |
        | Satisfaction | 2.0 → 3.5 |
        | Silent Churn | -40% |
        | Adoption | 70% |
        """)
    
    st.markdown("---")
    st.subheader("🔄 Design Iterations")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **❌ What Didn't Work:**
        - In-meeting pop-ups (disruptive)
        - 10-point scales (42% abandonment)
        - No opt-out (privacy concerns)
        """)
    
    with col2:
        st.markdown("""
        **✅ What We Learned:**
        - Post-meeting only
        - 3-point emoji scale optimal
        - Privacy controls build trust
        """)


# ============ PAGE 5: RESULTS ============
elif page == "📈 Results":
    st.title("📈 Results & Impact")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.metric("Satisfaction", "2.0 → 4.2", "+110%")
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.metric("Feedback Rate", "5% → 68%", "+1260%")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.metric("Silent Churn", "15% → 6%", "-60%")
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.metric("Renewal Rate", "82% → 94%", "+12%")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col3:
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.metric("Revenue Protected", "$4.2M", "Annual")
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.metric("Support Tickets", "-60%", "Bug-related")
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Before vs After chart
    df_results = pd.DataFrame({
        'Metric': ['Satisfaction', 'Feedback Rate', 'Silent Churn', 'Renewal'],
        'Before': [2.0, 5, 15, 82],
        'After': [4.2, 68, 6, 94]
    })
    
    fig = px.bar(df_results, x='Metric', y=['Before', 'After'],
                 barmode='group', title='Key Metrics: Before vs After',
                 color_discrete_map={'Before': '#EF4444', 'After': '#10B981'})
    st.plotly_chart(fig, use_container_width=True)


# ============ PAGE 6: LEARNINGS ============
else:
    st.title("🎓 Learnings & Conclusion")
    
    st.markdown("""
    ## Key Takeaways
    
    This project taught me that the most critical user problems are often the quietest ones.
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### ✅ What Went Well
        
        1. **Problem Discovery** - Identified silent churn before it escalated
        2. **Research Depth** - 24 interviews revealed workaround patterns
        3. **Stakeholder Alignment** - Got CEO, CTO, Design on same page
        4. **MVP Focus** - Shipped in 4 weeks, iterated based on feedback
        """)
    
    with col2:
        st.markdown("""
        ### 🚧 Challenges Overcome
        
        1. **Silent Users** - Shifted from surveys to behavioral signals
        2. **Technical Debt** - Balanced new features with stability
        3. **UX Concerns** - Proved passive feedback doesn't disrupt
        4. **Privacy** - Built opt-out controls, increased adoption
        """)
    
    st.markdown("---")
    st.markdown("""
    ### 💭 Final Reflection
    
    **The biggest lesson:** Users vote with their behavior, not their words.
    
    By building a system that listens to silent cues of dissatisfaction, we didn't just solve a feature gap—
    we rebuilt trust with our most valuable clients.
    
    This project established a **data-driven feedback culture** at Sync that continues to inform product decisions today.
    """)
    
    st.balloons()
    st.success("✅ Thank you for reviewing my portfolio case study!")


# Footer
st.markdown("---")
st.markdown("<div style='text-align: center; color: #6B7280;'>📊 Sync Product Case Study | Product Management Portfolio | 2024</div>", unsafe_allow_html=True)