# KYC Automation Example in R
# This script demonstrates a simple KYC risk scoring process
library(dplyr)

# Sample data: customers with age, country, and politically exposed person flag
customers <- data.frame(
  customer_id = 1:6,
  age = c(22, 45, 65, 30, 55, 18),
  country = c("UAE", "USA", "Iran", "India", "Russia", "UK"),
  pep_flag = c(FALSE, TRUE, FALSE, FALSE, TRUE, FALSE)
)

# Define high risk countries
high_risk_countries <- c("Iran", "Russia", "North Korea", "Syria")

# Perform risk scoring: flagged if age > 60, PEP or high risk country
customers <- customers %>%
  mutate(
    high_risk = ifelse(age > 60 | pep_flag | country %in% high_risk_countries, TRUE, FALSE)
  )

print(customers)
