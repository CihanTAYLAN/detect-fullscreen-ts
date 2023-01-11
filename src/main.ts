import { isFullscreen } from '../build/Release/Fullscreen.node';
export default (): boolean => {
  return isFullscreen();
};
