import json
d = {"frames": {}, "meta": {}}


for i in range(17):
    s = "water"+str(i+1)+".png"
    d["frames"][s] = {
        "frame": {
            "x": int(i*45),
            "y": 0,
            "w": 45,
            "h": 45
        }, "rotated": False,
        "trimmed": False,
        "spriteSourceSize": {
            "x": int(i*45),
            "y": 0,
            "w": 45,
            "h": 45
        },
        "sourceSize": {
            "w": 45,
            "h": 45
        },
        "pivot": {
            "x": 0.5,
            "y": 0.5
        }
    }

d["meta"] = {
    "app": "custom python script",
    "version": "1.0",
    "image": "water.png",
    "format": "RGBA8888",
    "size": {
        "w": int(17*45),
        "h": 45
    },
    "scale": "1",
    "smartupdate": "$TexturePacker:SmartUpdate:51ede84c7a85e4d6aeb31a6020a20858:3923663e59fb40b578d66a492a2cda2d:9995f8b4db1ac3cb75651b1542df8ee2$"
}

with open("yeah.json","w") as f:
    f.write(json.dumps(d))
