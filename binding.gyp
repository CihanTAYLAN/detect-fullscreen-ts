{
  "targets": [
    {
      "target_name": "Fullscreen",
      "sources": [ "src/node-addon/fullscreen.cc" ],
      'cflags': [
        '-Wall',
        '-Wparentheses',
        '-Winline',
        '-Wbad-function-cast',
        '-Wdisabled-optimization',
        '-std=c++17'
      ],
      'cflags_cc': [
        '-std=c++17'
      ],
      'conditions': [
        ['OS == "mac"', {
          'sources': [
            'src/node-addon/mac/fullscreen.mm'
          ],
          'include_dirs': [
            'System/Library/Frameworks/Carbon.Framework/Headers'
          ],
          'link_settings': {
            'libraries': [
              '-framework Carbon',
              '-framework AppKit',
            ]
          },
          'xcode_settings': {
            'OTHER_CFLAGS': [
                '-ObjC++'
            ]
          }
        }],
        ["OS=='win'", {
          'sources': [
            'src/node-addon/win/fullscreen.cc'
          ],
          'msvs_settings': {
            'VCCLCompilerTool': { "ExceptionHandling": 1, 'AdditionalOptions': [ '-std:c++17' ] }
          }
        }],
        ["OS=='linux'", {
          'sources': [
            'src/node-addon/unsupported/fullscreen.cc'
          ]
        }]
      ]
    }
  ]
}
