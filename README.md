# ivda
## front
/src/components: contains 5 files which represent 5 modules in the dashboard.
/src/App.vue: the main entrance of our project

## backend
/src/__init__.py: the PredictPrice(Resource) method receives features from frontend.
Other files and methods are not relevant to the current project. But it might provide a guide to current work.

# Instructions:
## Prepare for the running:

### Project setup
```
npm install
```

### prepare the file? for a map
```
npm install leaflet vue2-leaflet --save
```

### prepare the file? for a histogram
```
npm i vue-histogram-slider
```

### go to the front folder
```
cd front
```
## to start the frontend server:
```
npm run serve
```

### Compiles and minifies for production
```
npm run build
```

### Lints and fixes files
```
npm run lint
```

## To run the backend:
```
cd backend
bash commands.sh
```

### Customize configuration
See [Configuration Reference](https://cli.vuejs.org/config/).
