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
### Installation
```bash
pip install UnityPyTypetreeCodegen
```
### Generating code
- You can generate code from a TypeTree JSON dump generated with https://github.com/K0lb3/TypeTreeGenerator
```bash
UnityPyTypetreeCodegen --json "path_to_typetree_json_dump" --output "generated_moudle_path"
```
- Or dump the TypeTree using https://github.com/UnityPy-Org/TypeTreeGeneratorAPI automatically (WIP)
```bash
UnityPyTypetreeCodegen --files "path_to_Assembly-CSharp_and_other_mono_dlls" --output "generated_moudle_path"
```
- The emitted module will be structured like this
```
generated
├── __init__.py
└── Live2D
    └── Cubism
        ├── Core
        │   ├── __init__.py
        │   └── Unmanaged
        │       └── __init__.py
        ├── Framework
        │   ├── __init__.py
        │   ├── Expression
        │   │   └── __init__.py
        │   ├── HarmonicMotion
        │   │   └── __init__.py
        │   ├── Json
        │   │   └── __init__.py
        │   ├── LookAt
        │   │   └── __init__.py
        │   ├── Motion
        │   │   └── __init__.py
        │   ├── MotionFade
        │   │   └── __init__.py
        │   ├── MouthMovement
        │   │   └── __init__.py
        │   ├── Physics
        │   │   └── __init__.py
        │   ├── Pose
        │   │   └── __init__.py
        │   ├── Raycasting
        │   │   └── __init__.py
        │   ├── Tasking
        │   │   └── __init__.py
        │   └── UserData
        │       └── __init__.py
        └── Rendering
            ├── __init__.py
            └── Masking
                └── __init__.py

20 directories, 18 files
```
### Using the generated module
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