# Use the official Python image as the base image
FROM python:3.8

# Set the working directory in the container
WORKDIR /app

# Copy the application files into the working directory
COPY requirements.txt ./requirements.txt

# Install the application dependencies
RUN pip install -r requirements.txt

EXPOSE 8501

COPY . /app


# Define the entry point for the container
ENTRYPOINT ["streamlit","run"]
CMD ["app.py"]
