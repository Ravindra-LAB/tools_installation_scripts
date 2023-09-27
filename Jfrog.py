import subprocess

def upload_jar_to_artifactory(/home/ubuntu/Java_app_3.0/target, http://3.145.190.3:8082/ui/admin/onboarding-page, http://3.145.190.3:8082/ui/admin/repositories/local):
    try:
        # Construct the JFrog CLI upload command
        command = [
            'jfrog',
            'rt',
            'u',
            jar_file_path,
            f'{repository_url}/{target_path}/{jar_file_path}'
        ]

        # Run the JFrog CLI upload command
        subprocess.run(command, check=True)
        print(f'Successfully uploaded {jar_file_path} to {repository_url}/{target_path}')
    except subprocess.CalledProcessError as e:
        print(f'Error: {e}')

if __name__ == '__main__':
    # Specify the path to your JAR file
    jar_file_path = 'path/to/your.jar'

    # Replace these with your Artifactory repository URL and target path
    repository_url = 'https://your-artifactory-repo-url'
    target_path = 'path/in/repository'

    upload_jar_to_artifactory(jar_file_path, repository_url, target_path)
