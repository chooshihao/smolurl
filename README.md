# SmolURL

A Flask web application that allows users to shorten URLs.

## Getting Started

#### 0. Create an environment (Optional)
```
conda create -n smolurl python=3.9
conda activate smolurl
```

#### 1. Install Python dependencies
```
pip install -r requirements.txt
```

#### 2. Download Bootstrap 5.2.1
Static pages have been configured to use Bootstrap via CDN but you may wish to download it and put it in [app/static folder](app/static).

#### 3. Configure the app
Update [app.conf](app/app.conf) accordingly. <br>
If you wish to use the app locally, you need only update the <i>db_uri</i> field. <br>

Example using sqlite database:
```
[default]
host = 0.0.0.0
port = 8000
db_uri = sqlite:///foo.db
debug = 1
```
Example using MySQL database:
```
[default]
host = 0.0.0.0
port = 8000
db_uri = mysql://username:password@localhost:3306/yourdatabase
debug = 1
```

#### 4. Run the application

```
python main.py
```

## Usage Screenshots
<kbd>
  <img src="https://user-images.githubusercontent.com/15900094/189582245-9fdb4be2-c0c2-4065-8d5c-b9af33c23450.png" height="576" width="1024">
</kbd>
<br>
<br>
<kbd>
  <img src="https://user-images.githubusercontent.com/15900094/189582295-1d02dc03-a926-4fff-82e3-d57b61b969b8.png" height="576" width="1024">
</kbd>
