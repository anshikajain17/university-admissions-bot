# 📘 Project Documentation
## University Admissions AI Assistant

---

## 1. Project Overview

The **University Admissions AI Assistant** is a production-ready AI-powered web application designed to help students understand university admission requirements quickly and clearly.

The application dynamically compresses long admission-related information using the **ScaleDown API**, based on user-selected compression levels (Low / Medium / High).

This project was developed as part of the **Gen AI for Gen Z Challenge (Intel Unnati × HPE × ScaleDown)**.

---

## 2. Problem Statement

University admission information is often lengthy, complex, and difficult to interpret.

Students face challenges such as:
- Extracting eligibility criteria
- Identifying important dates
- Understanding document requirements

---

## 3. Solution Approach

The application follows this workflow:

1. Admission data is stored in a structured text format.
2. The user enters a query related to admissions.
3. The user selects a compression level.
4. The selected content is sent to the ScaleDown API.
5. The API compresses the text while preserving meaning.
6. The optimized response is displayed to the user.

This ensures clarity without information loss.

---

## 4. Key Features

- AI-powered dynamic text compression
- Adjustable compression levels (Low / Medium / High)
- Secure API key handling using environment variables
- Production-ready cloud deployment
- Clean and professional user interface
- Well-documented codebase with screenshots and demo preview

---

## 5. Technology Stack

- Backend: Python, Flask
- AI Service: ScaleDown API
- Web Server: Gunicorn
- Deployment Platform: Render
- Version Control: Git & GitHub
- Security: Environment Variables

---

## 6. Application Architecture

- Frontend: HTML & CSS using Flask templates
- Backend: Flask routes and API handling
- Data Layer: Local admission data file
- AI Layer: ScaleDown API for text compression
- Deployment Layer: Gunicorn + Render Cloud

---

## 7. Security Considerations

- API keys are not hardcoded
- Environment variables are used for sensitive data
- Secure deployment practices are followed

---

## 8. Deployment Details

- Hosted on Render (Free Tier)
- Uses Gunicorn as the production WSGI server
- Live demo link provided in README

Note:
Due to free-tier hosting, the application may take 30–50 seconds to respond on first request after inactivity.

---

## 9. Limitations

- Cold start delay due to free hosting
- Static admission data
- No authentication system (out of scope)

---

## 10. Future Enhancements

- Integration with real-time university databases
- User authentication and personalization
- Multilingual support
- Advanced AI query understanding
- Analytics dashboard

---

## 11. Conclusion

This project demonstrates end-to-end implementation of an AI-powered web application, covering:

- Backend development
- AI API integration
- Secure configuration
- Cloud deployment
- Documentation and version control

It reflects practical, production-oriented engineering skills.

---

## 12. Author

**Anshika Jain**  
Software Engineering Student  

- GitHub: https://github.com/anshikajain17  
- LinkedIn: https://www.linkedin.com/in/anshika-jain-a42b06292/

