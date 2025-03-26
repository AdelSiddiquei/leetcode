# Start from a lightweight base image with conda pre-installed
FROM continuumio/miniconda3:latest

# Set working directory
WORKDIR /app

# Copy environment file first (for better caching)
COPY environment.yaml .

# Create Conda environment (cached unless environment.yml changes)
RUN conda env create -f environment.yaml

# Copy everythinge else, can be split up if project becomes larger.
COPY . .

# Command to run when container starts, in this case it is designed to keep container running forever.
CMD ["tail", "-f", "/dev/null"]