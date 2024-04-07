# References
[Teen Profiles: Gen Z Research](https://business.yougov.com/content/37173-teen-profiles-gen-z-research)

[Gen Z: Challenges and Opportunities on Social Media](https://today.yougov.com/consumer/articles/38335-gen-z-challenge-and-opportunities-social-media-mar?redirect_from=%2Ftopics%2Fconsumer%2Farticles-reports%2F2021%2F09%2F07%2Fgen-z-challenge-and-opportunities-social-media-mar)

[What Age Do Kids Get Phones, Tablets, Laptops?](https://yougov.co.uk/society/articles/28368-what-age-do-kids-get-phones-tablet-laptops-)

[Meet the Next Consumer: How Gen Z are Taking New Reality](https://www.thedrum.com/news/2020/11/03/meet-the-next-consumer-how-gen-z-are-taking-new-reality)

[The Next Next Consumer: Understanding Gen Z](https://www.mckinsey.com/~/media/mckinsey/email/genz/2022/11/29/2022-11-29b.html)

[How Leading Questions and Acquiescence Bias Can Impact Surveys](https://yougov.co.uk/politics/articles/45308-how-leading-questions-and-acquiescence-bias-can-im)

[Strategies for Capitalizing on Gen Z's Growing Influence](https://www.forbes.com/sites/forbesbusinesscouncil/2024/03/06/strategies-for-capitalizing-on-gen-zs-growing-influence/?sh=431986691619)

Teen Profiles: Gen Z Research

Gen Z: Challenges and Opportunities on Social Media

What Age Do Kids Get Phones, Tablets, Laptops?

Meet the Next Consumer: How Gen Z are Taking New Reality

The Next Next Consumer: Understanding Gen Z

How Leading Questions and Acquiescence Bias Can Impact Surveys

Strategies for Capitalizing on Gen Z's Growing Influence


# Market Research Challenge

This repository contains the solution to the Inversity Challenge titled "Reimagining Market Research: How can technology help us work out what people are thinking and turn these insights into action?".

## Getting Started

To run the application locally, you can use Docker to build and compose the app.

### Prerequisites

Make sure you have Docker installed on your local machine. You can download and install Docker from the [official Docker website](https://www.docker.com/products/docker-desktop).

### Setup

1. **Environment Variables**: Create a `.env` file in the backend directory. Copy the contents of `template.env` to `.env` and update the variables according to your environment. You will need an OpenAI key from the [openAI website](https://platform.openai.com/)

2. **Build Docker Image**: Navigate to the root directory of the project and run the following command to build the Docker image:

    ```bash
    docker build -t market-research-app .
    ```

   This command builds a Docker image named `market-research-app` based on the Dockerfile in the project directory.

3. **Run Docker Compose**: After successfully building the Docker image, use Docker Compose to start the application. Run the following command:

    ```bash
    docker-compose up
    ```

   This command starts the application defined in the `docker-compose.yml` file, including any necessary services and dependencies.

4. **Access the App**: Once Docker Compose has started the application, you can access it in your web browser by navigating to [http://localhost:5000](http://localhost:5000).

## Contributing

Contributions are welcome! Please feel free to fork the repository, make changes, and submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE). Feel free to use, modify, and distribute the code for your own purposes.
