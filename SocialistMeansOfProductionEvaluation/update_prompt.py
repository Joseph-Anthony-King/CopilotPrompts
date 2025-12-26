import re

# Read the file
with open(r'c:\Users\Joe\Source\repos\CopilotPrompts\SocialistMeansOfProductionEvaluation\prompt.md', 'r', encoding='utf-8') as f:
    content = f.read()

# Define the old text pattern (using regex to handle special chars)
old_pattern = r'When credits are issued as capital outlays they can pay for services, not goods, at the time of their issuance as the credits have value due to work being performed\.  As an example, suppose a social worker wanted to distribute sandwiches\.  The Peoples. Bank can issue capital outlays to cover the social workers work, but not the sandwich as the sandwich.s creation was covered by prior credits when it was created\.'

# New text
new_text = 'When credits are issued as capital outlays, they compensate for new work being performed at the time of issuance, consistent with the labor theory of value. To be clear, goods can be purchased with credits throughout the economy; however, capital outlays specifically fund the labor being performed, not goods that were already produced and compensated. As an example, suppose a social worker wanted to distribute sandwiches for charitable purposes. The Peoples\' Bank can issue capital outlays to directly fund the social worker\'s labor, while the sandwiches themselves would be purchased normally with credits through the economy—the sandwich cooperative was already compensated when they produced the sandwiches. This ensures that work is compensated once based on the labor theory of value, avoiding double-payment for work already performed.'

# Replace
content = re.sub(old_pattern, new_text, content)

# Write back
with open(r'c:\Users\Joe\Source\repos\CopilotPrompts\SocialistMeansOfProductionEvaluation\prompt.md', 'w', encoding='utf-8') as f:
    f.write(content)

print('Replacement complete')
