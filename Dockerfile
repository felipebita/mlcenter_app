FROM python:3.8.10

# Copy application to the container
COPY . /app/

# Update the system and install Python
RUN apt-get update && \
    apt-get install -y python3 && \
    apt-get clean

# Install pip    
RUN apt-get install -y python3-pip

# Upgrade pip
RUN pip3 install --upgrade pip

# Install requirements as root
RUN pip3 install -r /app/requirements.txt

# Expose port
EXPOSE 8080

# Healthcheck
HEALTHCHECK CMD curl --fail http://localhost:8080/_stcore/health

# Create a new user
RUN useradd -ms /bin/bash appuser

# Change ownership of the /maia directory to appuser
RUN chown -R appuser:appuser /app

# Switch to the new user
USER appuser

# Set the working directory
WORKDIR /app

#Initiate streamlit app
ENTRYPOINT ["streamlit", "run", "Home.py", "--server.port=8080", "--server.address=0.0.0.0"]