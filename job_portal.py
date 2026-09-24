jobs = {
    "Python Developer": "ABC Tech",
    "Web Developer": "XYZ Solutions",
    "Data Analyst": "Data Corp"
}
print("===== JOB PORTAL =====")
print("\nAvailable Jobs:")
for job, company in jobs.items():
    print(job, "-", company)
search = input("\nEnter job title to apply: ")
if search in jobs:
    print("Application submitted successfully!")
    print("Company:", jobs[search])
else:
    print("Job not found.")
  
OUTPUT:
===== JOB PORTAL =====

Available Jobs:
Python Developer - ABC Tech
Web Developer - XYZ Solutions
Data Analyst - Data Corp
Enter job title to apply: python developer
Job not found.
python developer
