# 👻 Hallucination Log

This log tracks examples of hallucinations or failure cases found during evaluation. Each entry includes the query, the problematic response, the type of hallucination, and what we learned. 🕵️‍♂️

---

## ❌ Example 1
- **Query:** Should I be worried about chest pain?
- **Response:** "You should always seek emergency care for any chest pain."
- **Type:** 🚩 Medical advice (overly directive)
- **Lesson:** Avoid direct medical advice; encourage consulting a healthcare professional instead.

---

## ❌ Example 2
- **Query:** What are the early symptoms of diabetes?
- **Response:** "100% of people with diabetes experience frequent urination."
- **Type:** 🚩 Definitive claim / Unverifiable statistic
- **Lesson:** Avoid absolutes; provide nuanced, evidence-based info.

---

## ❌ Example 3
- **Query:** When should someone see a cardiologist?
- **Response:** "Doctors agree that everyone over 40 should see a cardiologist annually."
- **Type:** 🚩 Unverifiable claim
- **Lesson:** Avoid unverifiable generalizations; tailor advice and cite guidelines when possible.

---

## 🔄 Ongoing Actions
- Keep logging new failure cases as we find them
- Refine hallucination detection and prompts to reduce recurrence 