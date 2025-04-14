UnityPyTypetreeCodegen
---
(WIP) Static TypeTree code analysis and code generation for UnityPy

Used in 
- https://github.com/mos9527/UnityPyLive2DExtractor
    - Uses generated classes in https://github.com/mos9527/UnityPyLive2DExtractor/tree/main/UnityPyLive2DExtractor/generated
- https://github.com/mos9527/sssekai/
    - Used for AppHash in https://github.com/mos9527/sssekai/tree/main/sssekai/generated
- https://github.com/mos9527/sssekai_blender_io/
    - Used for TransportDefine in https://github.com/mos9527/sssekai_blender_io/tree/master/scripts/rla_transport_defines/generated
## Usage
Example usage in `rla_transport_defines`
```python
env = UnityPy.load(...)
from generated import UTTCGen_AsInstance, UTTCGen_GetClass

for reader in filter(lambda x: x.type == ClassIDType.MonoBehaviour, env.objects):
    name = reader.peek_name()
    if name.startswith("TransportDefine"):        
        from generated.Sekai.Streaming import TransportDefine
        # ...or TransportDefine = UTTCGen_GetClass("Sekai.Streaming.TransportDefine")
        # ...or TransportDefine = UTTCGen_GetClass(reader.read(check_read=False))
        instance = UTTCGen_AsInstance(TransportDefine, reader)                
        print(f'"{name}":({instance.validBones}, {instance.validBlendShapes}),')
        # Possibly modify on the instance itself and saving it is also possible
        instance.validBones[0] = "BadBone"
        instance.save()
env.save()
```