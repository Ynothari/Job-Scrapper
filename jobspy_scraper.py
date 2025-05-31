from jobspy import scrape_jobs

# Define your search parameters
jobs = scrape_jobs(
    site_name=["linkedin", "indeed"],  # add more if needed
    search_term="cloud aws devops ai generative ai",
    location="Chennai, India",
    results_wanted=50,
    distance=50,
    country_indeed="India",  # Optional but useful
    linkedin_job_type="internship",  # Optional: full-time, internship, etc.
)

# Export to CSV
jobs.to_csv("jobs.csv", index=False)
print("✅ Job scraping complete. Results saved to jobs.csv.")
