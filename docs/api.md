## List

**Endpoint**: GET - http://127.0.0.1:3306/air/list?page=0&limit=10

**Description**: get air record list

#### Header
```
{
}
```


#### Body
```

```

## Create

**Endpoint**: POST - http://127.0.0.1:3306/air/create

**Description**: upload an air record

#### Header
```
{
	Content-Type: application/json; charset=utf-8
}
```


#### Body
```
{
	"pm10": "60",
	"pm25": "105",
	"so2": "2",
	"co": "5 ",
	"no2": "20",
	"date": "2021-11-13"
}
```

## Forecast

**Endpoint**: GET - http://127.0.0.1:3306/air/forecast

**Description**: Room air quality forecast

#### Header
```
{
}
```


#### Body
```

```

