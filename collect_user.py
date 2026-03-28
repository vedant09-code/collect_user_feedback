#collecting a user feedback

feedback=["Great service!","Very Satisfied","Could be better","Excellent Experience"]

#Adding New feedback

feedback.append("Not Happy with the service")

#Counting specific feedback

positive_feedback_count=sum(1 for comment in feedback if "great" or "excellent" in comment.lower())

print(f"Positive Feedback count:{positive_feedback_count}")

#printing all the feedback

print("User Feedback:")
for comment in feedback:
    print(f"-{comment}")