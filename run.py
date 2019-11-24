from DemoApp import create_app

if __name__ == "__main__":
    app = create_app("config")
    
    app.run(debug=False,port=9999,host='0.0.0.0')
