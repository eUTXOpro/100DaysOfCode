import Graphics.Win32

-- Define the window procedure, which handles messages sent to the window
wndProc :: HWND -> WindowMessage -> WPARAM -> LPARAM -> LRESULT
wndProc hwnd msg wparam lparam =
    case msg of
        -- Handle the WM_CLOSE message by destroying the window
        WM_CLOSE ->
            destroyWindow hwnd

        -- Handle the WM_DESTROY message by quitting the application
        WM_DESTROY ->
            postQuitMessage 0

        -- Handle all other messages by calling the default window procedure
        _ ->
            defWindowProc (Just hwnd) msg wparam lparam

main :: IO ()
main = do
    -- Register the window class
    let windowClass =
            mkClassName "MyWindowClass"
    icon         <- loadIcon   Nothing IDI_APPLICATION
    cursor       <- loadCursor Nothing IDC_ARROW
    classAtom    <- registerClass
        ( cS_VREDRAW + cS_HREDRAW
        , Nothing
        , Just cursor
        , Just icon
        , Just $ blackBrush
        , windowClass
        )

    -- Create the window
    let windowTitle = "My Window"
    hwnd <- createWindow
        windowClass
        windowTitle
        wS_OVERLAPPEDWINDOW
        Nothing
        Nothing
        400
        300
        Nothing
        Nothing
        classAtom
        Nothing
        wndProc

    -- Show the window
    showWindow hwnd sW_SHOWNORMAL

    -- Run the message loop
    allocaMessage $ \msg ->
        let
            loop = do
                -- Get the next message
                getMessage msg Nothing

                -- Translate and dispatch the message
                translateMessage msg
                dispatchMessage msg

                -- Continue the loop if the message is not WM_QUIT
                messageWM_QUIT <- peekMessage msg (Just $ hwnd) (0, 0, 0, 0)
                unless messageWM_QUIT loop
        in
            loop