# Sales Data Reconciliation & Reporting Accuracy

A sample analysis project demonstrating how I approach reconciling sales figures across two independent reporting systems — a common data quality problem for any company that pulls numbers from more than one platform (e.g. a distributor dashboard vs. a CRM/sales system).

> Note: This project uses fully synthetic, randomly generated data for demonstration purposes. It is modeled on the structure and approach of real reconciliation work I've done professionally, but contains no confidential or client data.
>
> ## The Problem
>
> When two systems are supposed to report the same underlying sales activity, small "acceptable" gaps often mask real, fixable issues — timing lag in when a partner reports, inconsistent treatment of discounts/samples, or mapping errors between product codes. Left unexamined, these gaps erode trust in whichever number leadership is using to make decisions.
>
> ## What This Project Does
>
> 1. Generates sample data (generate_sample_data.py) simulating two reporting systems tracking the same sales across month, SKU, region, and distributor — with a deliberate, realistic bias baked in.
> 2. 2. Reconciles the two systems (reconcile.py): calculates the overall gap, breaks it down by month, distributor, and region, and outputs summary tables plus a chart ready to share with stakeholders.
>   
>    3. ## Sample Finding
>   
>    4. In this simulated dataset, the two systems tie out to within 2.5% overall — but that headline number hides the real story: two distributors (A and C) consistently report 5-6% higher in System B, while the other two are within 1%. That's the kind of pattern that turns a vague 'the numbers don't match' into a specific, actionable finding.
>   
>    5. This mirrors the actual reconciliation approach I use in practice: don't just report the gap — isolate where it concentrates, and let that point to the root cause.
>
>    6. ## Tech Used
>
>    7. - Python (pandas for data manipulation, matplotlib for visualization)
>       - - Designed to translate directly to Power BI / SQL workflows — the groupby/aggregation logic here is the same logic I'd implement as DAX measures or SQL GROUP BY queries in a live BI tool
>        
>         - ## Run It Yourself
>        
>         - pip install pandas matplotlib
>         - python generate_sample_data.py
>         - python reconcile.py
>
> ---
> Mark Jesson Esparagoza — Data Analyst | Power BI, SQL, Reporting Reconciliation
> 
